#!/usr/bin/env python3
"""
Generate v2 GraphQL docs from live schema introspection.

Outputs:
- skills/hive-api/docs/v2/graphql/index.md
- skills/hive-api/docs/v2/graphql/endpoints/{queries,mutations,subscriptions}/*.md
- skills/hive-api/docs/v2/graphql/schema.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import textwrap
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


INTROSPECTION_QUERY = """
query IntrospectionQuery {
  __schema {
    queryType { name }
    mutationType { name }
    subscriptionType { name }
    types {
      kind
      name
      description
      fields(includeDeprecated: true) {
        name
        description
        isDeprecated
        deprecationReason
        args {
          name
          description
          defaultValue
          type {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                  ofType {
                    kind
                    name
                    ofType {
                      kind
                      name
                      ofType {
                        kind
                        name
                      }
                    }
                  }
                }
              }
            }
          }
        }
        type {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                  ofType {
                    kind
                    name
                    ofType {
                      kind
                      name
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
""".strip()


def gql_type_to_string(type_node: dict[str, Any] | None) -> str:
    if not type_node:
        return "Unknown"
    kind = type_node.get("kind")
    name = type_node.get("name")
    of_type = type_node.get("ofType")
    if kind == "NON_NULL":
        return f"{gql_type_to_string(of_type)}!"
    if kind == "LIST":
        return f"[{gql_type_to_string(of_type)}]"
    return name or kind or "Unknown"


def md_escape(value: str | None) -> str:
    if not value:
        return ""
    return value.replace("\n", " ").replace("|", "\\|").strip()


def slugify(value: str) -> str:
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", value)
    value = re.sub(r"[^a-zA-Z0-9]+", "-", value).strip("-")
    return value.lower() or "unknown-operation"


def fetch_introspection(endpoint: str, token: str | None = None) -> dict[str, Any]:
    payload = json.dumps({"query": INTROSPECTION_QUERY}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(endpoint, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GraphQL introspection failed: HTTP {exc.code} - {details}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"GraphQL introspection request failed: {exc}") from exc

    decoded = json.loads(body)
    if decoded.get("errors"):
        raise RuntimeError(f"GraphQL introspection returned errors: {decoded['errors']}")
    data = decoded.get("data")
    if not data or "__schema" not in data:
        raise RuntimeError("GraphQL introspection returned no schema data.")
    return decoded


def load_schema(schema_input_path: str | None, endpoint: str, token: str | None) -> dict[str, Any]:
    if schema_input_path:
        schema_path = Path(schema_input_path)
        if not schema_path.exists():
            raise RuntimeError(f"Schema input not found: {schema_path}")
        return json.loads(schema_path.read_text(encoding="utf-8"))
    return fetch_introspection(endpoint, token=token)


def render_operation_markdown(
    operation: dict[str, Any],
    operation_kind: str,
    endpoint: str,
) -> str:
    lines: list[str] = []
    lines.append(f"# `{operation['name']}`")
    lines.append("")
    lines.append(f"- Type: `{operation_kind}`")
    lines.append(f"- Returns: `{gql_type_to_string(operation.get('type'))}`")
    lines.append(f"- Deprecated: {'yes' if operation.get('isDeprecated') else 'no'}")
    if operation.get("deprecationReason"):
        lines.append(f"- Deprecation reason: {md_escape(operation.get('deprecationReason'))}")
    lines.append(f"- Source endpoint: `{endpoint}`")
    lines.append("")

    description = operation.get("description")
    if description:
        lines.append("## Description")
        lines.append("")
        lines.append(md_escape(description))
        lines.append("")

    args = operation.get("args") or []
    lines.append("## Arguments")
    lines.append("")
    if args:
        lines.append("| Arg | Type | Default | Description |")
        lines.append("|---|---|---|---|")
        for arg in args:
            lines.append(
                "| "
                f"`{arg['name']}` | `{gql_type_to_string(arg.get('type'))}` | "
                f"{md_escape(arg.get('defaultValue') or '-')} | "
                f"{md_escape(arg.get('description') or '-')} |"
            )
    else:
        lines.append("No arguments.")
    lines.append("")

    lines.append("## Signature")
    lines.append("")
    arg_signatures = [
        f"{arg['name']}: {gql_type_to_string(arg.get('type'))}" for arg in args
    ]
    args_part = ", ".join(arg_signatures)
    lines.append(
        f"- `{operation['name']}({args_part})` -> "
        f"`{gql_type_to_string(operation.get('type'))}`"
    )
    lines.append("")

    return "\n".join(lines).strip() + "\n"


def render_operation_table(operations: list[dict[str, Any]], relative_dir: str) -> list[str]:
    lines: list[str] = []
    lines.append("| Operation | Args | Returns | Deprecated |")
    lines.append("|---|---|---|---|")

    for op in sorted(operations, key=lambda item: item["name"].lower()):
        args = op.get("args") or []
        arg_summary = ", ".join(
            f"`{arg['name']}: {gql_type_to_string(arg.get('type'))}`" for arg in args
        )
        if not arg_summary:
            arg_summary = "-"
        deprecated = "yes" if op.get("isDeprecated") else "no"
        file_name = f"{slugify(op['name'])}.md"
        lines.append(
            "| "
            f"[`{op['name']}`]({relative_dir}/{file_name})"
            f" | {arg_summary} | `{gql_type_to_string(op.get('type'))}` | {deprecated} |"
        )
    lines.append("")
    return lines


def render_section(
    operations: list[dict[str, Any]],
    heading: str,
    type_name: str,
    relative_dir: str,
) -> list[str]:
    lines: list[str] = []
    lines.append(f"## {heading}")
    lines.append("")
    lines.append(f"Root type: `{type_name}`")
    lines.append("")
    lines.append(f"Total operations: **{len(operations)}**")
    lines.append("")
    lines.extend(render_operation_table(operations, relative_dir))
    return lines


def build_index_markdown(schema: dict[str, Any], endpoint: str) -> str:
    data = schema["data"]["__schema"]
    type_map = {t["name"]: t for t in data["types"] if t.get("name")}

    query_type = (data.get("queryType") or {}).get("name")
    mutation_type = (data.get("mutationType") or {}).get("name")
    subscription_type = (data.get("subscriptionType") or {}).get("name")

    query_fields = (type_map.get(query_type, {}) or {}).get("fields") or []
    mutation_fields = (type_map.get(mutation_type, {}) or {}).get("fields") or []
    subscription_fields = (type_map.get(subscription_type, {}) or {}).get("fields") or []

    generated_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    lines: list[str] = []
    lines.append("# Hive GraphQL v2 Endpoint Reference")
    lines.append("")
    lines.append(
        "Auto-generated from live introspection of "
        f"`{endpoint}`."
    )
    lines.append("")
    lines.append(f"- Generated at: `{generated_at}`")
    lines.append(f"- Query operations: **{len(query_fields)}**")
    lines.append(f"- Mutation operations: **{len(mutation_fields)}**")
    lines.append(f"- Subscription operations: **{len(subscription_fields)}**")
    lines.append("")
    lines.append("Each operation has its own file under `endpoints/`.")
    lines.append("")

    if query_type:
        lines.extend(render_section(query_fields, "Queries", query_type, "endpoints/queries"))
    if mutation_type:
        lines.extend(
            render_section(mutation_fields, "Mutations", mutation_type, "endpoints/mutations")
        )
    if subscription_type:
        lines.extend(
            render_section(
                subscription_fields,
                "Subscriptions",
                subscription_type,
                "endpoints/subscriptions",
            )
        )

    return "\n".join(lines).strip() + "\n"


def build_legacy_index_markdown(index_relative_path: str) -> str:
    return (
        "# Hive GraphQL v2 Endpoint Reference\n\n"
        "This file moved to a versioned docs folder.\n\n"
        f"- New location: [{index_relative_path}]({index_relative_path})\n"
    )


def write_operation_files(
    operations: list[dict[str, Any]],
    output_dir: Path,
    operation_kind: str,
    endpoint: str,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for operation in sorted(operations, key=lambda item: item["name"].lower()):
        file_path = output_dir / f"{slugify(operation['name'])}.md"
        markdown = render_operation_markdown(operation, operation_kind, endpoint)
        file_path.write_text(markdown, encoding="utf-8")


def generate_docs(
    schema: dict[str, Any],
    endpoint: str,
    output_index_md: Path,
    output_endpoints_dir: Path,
) -> None:
    data = schema["data"]["__schema"]
    type_map = {t["name"]: t for t in data["types"] if t.get("name")}

    query_type = (data.get("queryType") or {}).get("name")
    mutation_type = (data.get("mutationType") or {}).get("name")
    subscription_type = (data.get("subscriptionType") or {}).get("name")

    query_fields = (type_map.get(query_type, {}) or {}).get("fields") or []
    mutation_fields = (type_map.get(mutation_type, {}) or {}).get("fields") or []
    subscription_fields = (type_map.get(subscription_type, {}) or {}).get("fields") or []

    if output_endpoints_dir.exists():
        shutil.rmtree(output_endpoints_dir)
    output_endpoints_dir.mkdir(parents=True, exist_ok=True)

    if query_type:
        write_operation_files(
            query_fields,
            output_endpoints_dir / "queries",
            operation_kind="query",
            endpoint=endpoint,
        )
    if mutation_type:
        write_operation_files(
            mutation_fields,
            output_endpoints_dir / "mutations",
            operation_kind="mutation",
            endpoint=endpoint,
        )
    if subscription_type:
        write_operation_files(
            subscription_fields,
            output_endpoints_dir / "subscriptions",
            operation_kind="subscription",
            endpoint=endpoint,
        )

    output_index_md.parent.mkdir(parents=True, exist_ok=True)
    output_index_md.write_text(build_index_markdown(schema, endpoint), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate v2 GraphQL docs from live schema introspection."
    )
    parser.add_argument(
        "--endpoint",
        default="https://prod-gql.hive.com/graphql",
        help="GraphQL endpoint URL.",
    )
    parser.add_argument(
        "--token",
        default=None,
        help="Optional bearer token for Authorization header.",
    )
    parser.add_argument(
        "--schema-input",
        default=None,
        help="Optional existing introspection JSON path. If set, skips network fetch.",
    )
    parser.add_argument(
        "--output-index-md",
        default="skills/hive-api/docs/v2/graphql/index.md",
        help="Output v2 markdown index path.",
    )
    parser.add_argument(
        "--output-endpoints-dir",
        default="skills/hive-api/docs/v2/graphql/endpoints",
        help="Output directory for per-operation markdown files.",
    )
    parser.add_argument(
        "--output-schema-json",
        default="skills/hive-api/docs/v2/graphql/schema.json",
        help="Output raw v2 schema JSON file path.",
    )
    parser.add_argument(
        "--legacy-output-md",
        default="skills/hive-api/docs/graphql-v2-endpoints.md",
        help="Legacy v2 markdown location to keep as pointer.",
    )
    parser.add_argument(
        "--legacy-output-schema-json",
        default="skills/hive-api/docs/graphql-v2-schema.json",
        help="Legacy schema location to mirror for compatibility.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    schema = load_schema(args.schema_input, args.endpoint, args.token)

    output_index_md_path = Path(args.output_index_md)
    output_endpoints_dir_path = Path(args.output_endpoints_dir)
    output_schema_json_path = Path(args.output_schema_json)
    legacy_output_md_path = Path(args.legacy_output_md)
    legacy_output_schema_json_path = Path(args.legacy_output_schema_json)

    output_index_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_schema_json_path.parent.mkdir(parents=True, exist_ok=True)
    legacy_output_md_path.parent.mkdir(parents=True, exist_ok=True)
    legacy_output_schema_json_path.parent.mkdir(parents=True, exist_ok=True)

    generate_docs(
        schema=schema,
        endpoint=args.endpoint,
        output_index_md=output_index_md_path,
        output_endpoints_dir=output_endpoints_dir_path,
    )
    rendered_schema = json.dumps(schema, indent=2, ensure_ascii=True) + "\n"
    output_schema_json_path.write_text(rendered_schema, encoding="utf-8")
    legacy_output_schema_json_path.write_text(rendered_schema, encoding="utf-8")

    legacy_relative_target = output_index_md_path.relative_to(legacy_output_md_path.parent)
    legacy_output_md_path.write_text(
        build_legacy_index_markdown(legacy_relative_target.as_posix()),
        encoding="utf-8",
    )

    summary = textwrap.dedent(
        f"""
        Generated GraphQL v2 docs:
        - {output_index_md_path}
        - {output_endpoints_dir_path}
        - {output_schema_json_path}
        - {legacy_output_md_path} (pointer)
        - {legacy_output_schema_json_path} (mirrored)
        """
    ).strip()
    print(summary)


if __name__ == "__main__":
    main()
