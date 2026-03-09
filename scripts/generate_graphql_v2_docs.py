#!/usr/bin/env python3
"""
Generate v2 GraphQL docs from live schema introspection.

Outputs:
- skills/hive-api/docs/graphql-v2-endpoints.md
- skills/hive-api/docs/graphql-v2-schema.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
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


def render_operation_section(
    operations: list[dict[str, Any]],
    heading: str,
    type_name: str,
) -> list[str]:
    lines: list[str] = []
    lines.append(f"## {heading}")
    lines.append("")
    lines.append(f"Root type: `{type_name}`")
    lines.append("")
    lines.append(f"Total operations: **{len(operations)}**")
    lines.append("")

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
        lines.append(
            "| "
            f"`{op['name']}` | {arg_summary} | `{gql_type_to_string(op.get('type'))}` | {deprecated} |"
        )
    lines.append("")

    lines.append("### Details")
    lines.append("")
    for op in sorted(operations, key=lambda item: item["name"].lower()):
        lines.append(f"#### `{op['name']}`")
        lines.append("")
        description = op.get("description")
        if description:
            lines.append(md_escape(description))
            lines.append("")
        lines.append(f"- Returns: `{gql_type_to_string(op.get('type'))}`")
        if op.get("isDeprecated"):
            lines.append("- Deprecated: yes")
            if op.get("deprecationReason"):
                lines.append(f"- Deprecation reason: {md_escape(op['deprecationReason'])}")
        else:
            lines.append("- Deprecated: no")

        args = op.get("args") or []
        if args:
            lines.append("")
            lines.append("| Arg | Type | Default | Description |")
            lines.append("|---|---|---|---|")
            for arg in args:
                lines.append(
                    "| "
                    f"`{arg['name']}` | `{gql_type_to_string(arg.get('type'))}` | "
                    f"{md_escape(arg.get('defaultValue') or '-')} | "
                    f"{md_escape(arg.get('description') or '-')} |"
                )
        lines.append("")
    return lines


def build_markdown(schema: dict[str, Any], endpoint: str) -> str:
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
    lines.append("Use this reference as source-of-truth for available root operations and signatures.")
    lines.append("")

    if query_type:
        lines.extend(render_operation_section(query_fields, "Queries", query_type))
    if mutation_type:
        lines.extend(render_operation_section(mutation_fields, "Mutations", mutation_type))
    if subscription_type:
        lines.extend(render_operation_section(subscription_fields, "Subscriptions", subscription_type))

    return "\n".join(lines).strip() + "\n"


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
        "--output-md",
        default="skills/hive-api/docs/graphql-v2-endpoints.md",
        help="Output markdown file path.",
    )
    parser.add_argument(
        "--output-schema-json",
        default="skills/hive-api/docs/graphql-v2-schema.json",
        help="Output raw schema JSON file path.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    schema = fetch_introspection(args.endpoint, token=args.token)

    output_md_path = Path(args.output_md)
    output_schema_json_path = Path(args.output_schema_json)
    output_md_path.parent.mkdir(parents=True, exist_ok=True)
    output_schema_json_path.parent.mkdir(parents=True, exist_ok=True)

    markdown = build_markdown(schema, args.endpoint)
    output_md_path.write_text(markdown, encoding="utf-8")
    output_schema_json_path.write_text(
        json.dumps(schema, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )

    summary = textwrap.dedent(
        f"""
        Generated GraphQL v2 docs:
        - {output_md_path}
        - {output_schema_json_path}
        """
    ).strip()
    print(summary)


if __name__ == "__main__":
    main()
