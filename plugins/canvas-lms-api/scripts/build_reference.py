#!/usr/bin/env python3
"""Build the Canvas LMS API skill reference from the raw doc/api/ Swagger dump.

Deterministic, stdlib-only extractor. Reads the gitignored `doc/api/` source
(Swagger 1.2 JSON resource files + `file.*.html` prose guides) and regenerates
the committed `reference/` tree that the skill actually ships:

    reference/
      catalog.md              all resources: description, #endpoints, #models
      endpoints-index.md      one grep-able line per endpoint (~1,078 lines)
      resources/<slug>.md     per-resource: every endpoint (params/returns) + models
      guides/<topic>.md       extracted prose concept guides
      guides/README.md        guide index with one-line summaries
      permissions.md          consolidated RBAC permission descriptions

Usage (run from the plugin root, plugins/canvas-lms-api/):
    python3 scripts/build_reference.py [DOC_DIR] [OUT_DIR]

Defaults: DOC_DIR=<plugin>/doc/api, OUT_DIR=<plugin>/skills/canvas-lms-api/reference.
The output is a pure function of the input, so re-running is idempotent.
"""

from __future__ import annotations

import html
import json
import os
import re
import sys
from html.parser import HTMLParser

# Plugin root is one level up from scripts/. The generated reference lives inside
# the skill directory so it travels with the plugin when Claude Code copies it to
# the cache; the raw doc/ source stays at the plugin root and is gitignored.
PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DOC_DIR = os.path.join(PLUGIN_ROOT, "doc", "api")
DEFAULT_OUT_DIR = os.path.join(
    PLUGIN_ROOT, "skills", "canvas-lms-api", "reference"
)


# --------------------------------------------------------------------------- #
# HTML -> Markdown
# --------------------------------------------------------------------------- #

# The Canvas docs render every page inside <div id="content"> ... <div id="footer">.
# Everything else (nav sidebar, header, scripts) is boilerplate shared by all pages.
_CONTENT_RE = re.compile(r'<div id="content">(.*?)<div id="footer"', re.S)
# A "docs have moved" banner injected at the top of every page's content as a
# self-contained <div class="alert">...</div>.
_BANNER_RE = re.compile(r'<div class="alert">.*?</div>', re.S)


def slice_content(raw_html: str) -> str:
    """Return the inner content HTML (minus the redirect banner), or ''."""
    m = _CONTENT_RE.search(raw_html)
    if not m:
        return ""
    return _BANNER_RE.sub("", m.group(1), count=1)


class _MarkdownParser(HTMLParser):
    """Convert a fragment of Canvas doc HTML into readable Markdown.

    Handles the tag vocabulary actually used by these pages: h1-h6, p, br,
    ul/ol/li, dl/dt/dd, pre/code (fenced, language from class), table, a,
    strong/em, blockquote. script/style content is dropped.
    """

    _BLOCK = {"p", "div", "section", "article", "blockquote"}
    _SKIP = {"script", "style", "nav"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.out: list[str] = []
        self.skip_depth = 0
        # list context: stack of ("ul", None) / ("ol", counter)
        self.list_stack: list[list] = []
        # code context
        self.in_pre = False
        self.pre_lang = ""
        self.pre_buf: list[str] = []
        self.in_code = False
        # table context
        self.in_table = False
        self.table_rows: list[list[str]] = []
        self.cur_row: list[str] | None = None
        self.cur_cell: list[str] | None = None
        self.cell_is_header = False
        self.table_has_header = False
        self.in_blockquote = False

    # -- helpers ----------------------------------------------------------- #
    def _emit(self, text: str) -> None:
        if self.cur_cell is not None:
            self.cur_cell.append(text)
        else:
            self.out.append(text)

    def _newline_block(self) -> None:
        self.out.append("\n\n")

    # -- tag handlers ------------------------------------------------------ #
    def handle_starttag(self, tag, attrs):  # noqa: C901 - dispatch table
        if tag in self._SKIP:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        a = dict(attrs)

        if tag == "pre":
            self.in_pre = True
            self.pre_buf = []
            cls = a.get("class", "") or ""
            m = re.search(r"(?:language-|code\s+)([a-z0-9]+)", cls)
            self.pre_lang = m.group(1) if m else ""
            return
        if self.in_pre:
            return

        if tag == "code":
            self.in_code = True
            self._emit("`")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._newline_block()
            self._emit("#" * int(tag[1]) + " ")
        elif tag == "p":
            self._newline_block()
        elif tag == "br":
            self._emit("  \n")
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag == "ul":
            self.list_stack.append(["ul", 0])
        elif tag == "ol":
            self.list_stack.append(["ol", 0])
        elif tag == "li":
            self._start_li()
        elif tag == "dl":
            self._newline_block()
        elif tag == "dt":
            self.out.append("\n")
            self._emit("- **")
        elif tag == "dd":
            self.out.append("\n  ")
        elif tag == "blockquote":
            self._newline_block()
            self.in_blockquote = True
            self._emit("> ")
        elif tag == "a":
            self._href = a.get("href", "")
            if self._href.startswith("http"):
                self._emit("[")
        elif tag == "table":
            self.in_table = True
            self.table_rows = []
            self.table_has_header = False
        elif tag == "tr":
            self.cur_row = []
        elif tag in ("td", "th"):
            self.cur_cell = []
            self.cell_is_header = tag == "th"
            if tag == "th":
                self.table_has_header = True

    def handle_startendtag(self, tag, attrs):
        if tag == "br" and not self.in_pre and not self.skip_depth:
            self._emit("  \n")

    def handle_endtag(self, tag):  # noqa: C901
        if tag in self._SKIP:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return

        if tag == "pre":
            code = "".join(self.pre_buf).strip("\n")
            self.out.append("\n\n```" + self.pre_lang + "\n" + code + "\n```\n\n")
            self.in_pre = False
            self.pre_buf = []
            return
        if self.in_pre:
            return

        if tag == "code":
            self.in_code = False
            self._emit("`")
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._newline_block()
        elif tag == "p":
            self._newline_block()
        elif tag in ("strong", "b"):
            self._emit("**")
        elif tag in ("em", "i"):
            self._emit("*")
        elif tag in ("ul", "ol"):
            if self.list_stack:
                self.list_stack.pop()
            if not self.list_stack:
                self.out.append("\n")
        elif tag == "dt":
            self._emit("**")
        elif tag == "blockquote":
            self.in_blockquote = False
            self._newline_block()
        elif tag == "a":
            href = getattr(self, "_href", "")
            if href.startswith("http"):
                self._emit(f"]({href})")
        elif tag == "table":
            self._flush_table()
            self.in_table = False
        elif tag == "tr":
            if self.cur_row is not None:
                self.table_rows.append(self.cur_row)
            self.cur_row = None
        elif tag in ("td", "th"):
            if self.cur_row is not None and self.cur_cell is not None:
                self.cur_row.append("".join(self.cur_cell).strip())
            self.cur_cell = None

    def handle_data(self, data):
        if self.skip_depth:
            return
        if self.in_pre:
            self.pre_buf.append(data)
            return
        if not data:
            return
        # collapse whitespace outside code spans
        if self.in_code:
            self._emit(data)
        else:
            self._emit(re.sub(r"\s+", " ", data))

    # -- list / table plumbing -------------------------------------------- #
    def _start_li(self) -> None:
        depth = max(0, len(self.list_stack) - 1)
        indent = "  " * depth
        marker = "- "
        if self.list_stack and self.list_stack[-1][0] == "ol":
            self.list_stack[-1][1] += 1
            marker = f"{self.list_stack[-1][1]}. "
        self.out.append("\n" + indent + marker)

    def _flush_table(self) -> None:
        rows = [r for r in self.table_rows if r]
        if not rows:
            return
        ncol = max(len(r) for r in rows)
        rows = [r + [""] * (ncol - len(r)) for r in rows]
        if self.table_has_header:
            header, body = rows[0], rows[1:]
        else:
            header, body = [""] * ncol, rows
        lines = ["\n"]
        lines.append("| " + " | ".join(header) + " |")
        lines.append("| " + " | ".join(["---"] * ncol) + " |")
        for r in body:
            cells = [c.replace("\n", " ").replace("|", "\\|") for c in r]
            lines.append("| " + " | ".join(cells) + " |")
        lines.append("\n")
        self.out.append("\n".join(lines))


def _postprocess(md: str) -> str:
    md = re.sub(r"[ \t]+\n", "\n", md)          # trailing spaces (keep <br> two-space? drop)
    md = re.sub(r"\n{3,}", "\n\n", md)          # collapse blank runs
    md = re.sub(r"[ \t]{2,}", " ", md)          # collapse runs of spaces
    return md.strip() + "\n"


def html_to_markdown(fragment: str) -> str:
    p = _MarkdownParser()
    p.feed(fragment)
    p.close()
    return _postprocess("".join(p.out))


def guide_markdown(raw_html: str) -> str:
    """Extract a prose guide page as Markdown (banner already removed)."""
    return html_to_markdown(slice_content(raw_html)).strip() + "\n"


# --------------------------------------------------------------------------- #
# Resource (Swagger JSON) -> Markdown
# --------------------------------------------------------------------------- #

def _type_str(node: dict) -> str:
    """Human-readable type for a param/property node."""
    if not isinstance(node, dict):
        return ""
    if "$ref" in node:
        return node["$ref"]
    t = node.get("type", "")
    if t == "array":
        items = node.get("items") or {}
        inner = items.get("$ref") or items.get("type") or ""
        inner = re.sub(r"^\[|\]$", "", str(inner))  # some refs look like "[Integer]"
        return f"array[{inner}]" if inner else "array"
    fmt = node.get("format")
    return f"{t} ({fmt})" if fmt else t


def _clean(text) -> str:
    if text is None:
        return ""
    text = str(text).strip()
    text = text.replace("\r\n", "\n")
    # collapse internal newlines to spaces for table cells
    return text


def _cell(text) -> str:
    return _clean(text).replace("\n", " ").replace("|", "\\|")


def render_resource(res: dict, name: str) -> tuple[str, list[dict]]:
    """Return (markdown, endpoint_records) for one resource JSON doc."""
    out: list[str] = []
    out.append(f"# {name}\n")
    out.append(
        f"> Canvas LMS REST API — `{res.get('resourcePath', '')}` resource. "
        f"Base path `/api`.\n"
    )

    endpoints: list[dict] = []
    for api in res.get("apis", []):
        path = api.get("path", "")
        for op in api.get("operations", []):
            method = op.get("method", "")
            nickname = op.get("nickname", "")
            summary = op.get("summary", "") or nickname
            dep = op.get("deprecated")
            title = f"## {method} {path}"
            if dep:
                title += "  *(deprecated)*"
            out.append(title + "\n")
            out.append(f"**{summary}**  —  `{nickname}`\n")
            if dep and op.get("deprecation_description"):
                out.append(f"> ⚠️ Deprecated: {_clean(op['deprecation_description'])}\n")
            notes = _clean(op.get("notes"))
            if notes and notes != summary:
                out.append(notes + "\n")

            params = op.get("parameters", [])
            if params:
                out.append(_render_param_table(params))

            ret = _type_str({"type": op.get("type"), "items": op.get("items")})
            if ret:
                out.append(f"**Returns:** `{ret}`\n")

            endpoints.append(
                {
                    "method": method,
                    "path": path,
                    "nickname": nickname,
                    "summary": summary,
                    "deprecated": bool(dep),
                }
            )

    models = res.get("models") or {}
    if models:
        out.append("\n---\n\n# Models\n")
        for mname, model in models.items():
            out.append(_render_model(mname, model))

    return "\n".join(out).rstrip() + "\n", endpoints


def _render_param_table(params: list[dict]) -> str:
    lines = ["| Param | Type | In | Req | Description |", "| --- | --- | --- | --- | --- |"]
    for p in params:
        typ = _type_str(p)
        enum = p.get("enum")
        desc = _cell(p.get("description"))
        if enum:
            vals = ", ".join(f"`{v}`" for v in enum)
            desc = (desc + " " if desc else "") + f"Allowed: {vals}"
        req = "yes" if p.get("required") else ""
        name = p.get("name", "")
        if p.get("deprecated"):
            name += " *(dep)*"
        lines.append(
            f"| `{name}` | {typ} | {p.get('paramType', '')} | {req} | {desc} |"
        )
    return "\n".join(lines) + "\n"


def _render_model(name: str, model: dict) -> str:
    out = [f"\n## {name}\n"]
    desc = _clean(model.get("description"))
    if desc:
        out.append(desc + "\n")
    required = set(model.get("required") or [])
    props = model.get("properties") or {}
    if props:
        out.append("| Property | Type | Req | Description |")
        out.append("| --- | --- | --- | --- |")
        for pname, node in props.items():
            typ = _type_str(node)
            d = _cell(node.get("description") if isinstance(node, dict) else "")
            if isinstance(node, dict) and node.get("example") not in (None, ""):
                ex = _cell(node["example"])
                d = (d + " " if d else "") + f"e.g. `{ex}`"
            if isinstance(node, dict) and node.get("enum"):
                vals = ", ".join(f"`{v}`" for v in node["enum"])
                d = (d + " " if d else "") + f"Allowed: {vals}"
            req = "yes" if pname in required else ""
            out.append(f"| `{pname}` | {typ} | {req} | {d} |")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- #
# Permissions consolidation
# --------------------------------------------------------------------------- #

def permission_title(md: str, fallback: str) -> str:
    """First heading in a permission page is the human name of the permission."""
    m = re.search(r"^#+\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


# --------------------------------------------------------------------------- #
# Guide classification (for the guides index)
# --------------------------------------------------------------------------- #

GUIDE_GROUPS = [
    ("Core concepts", [
        "overview", "pagination", "object_ids", "endpoint_attributes", "throttling",
        "masquerading", "graphql", "changelog", "index", "developer_keys",
    ]),
    ("Authentication", [
        "oauth", "oauth_endpoints", "jwt_access_tokens",
    ]),
    ("Files & content", [
        "file_uploads", "content_item", "compound_documents", "document_processor",
    ]),
    ("SIS & bulk import", [
        "sis_csv", "provisioning", "outcomes_csv", "group_category_csv",
        "differentiation_tags_csv",
    ]),
    ("LTI & external tools", [
        "tools_intro", "tools_xml", "tools_variable_substitutions", "navigation_tools",
        "lti_launch_overview", "lti_dev_key_config", "lti_window_post_message",
        "registration", "plagiarism_platform", "originality_report_appendix",
        "placements_overview", "pns", "subscriptions_appendix", "canvas_roles",
        "assignment_tools", "assignment_selection_placement", "collaborations_placement",
        "editor_button_placement", "homework_submission_placement",
        "link_selection_placement", "migration_selection_placement", "xapi",
    ]),
    ("Live Events & Caliper (data services)", None),  # data_service_*
]


def classify_guide(topic: str) -> str:
    if topic.startswith("data_service"):
        return "Live Events & Caliper (data services)"
    for group, members in GUIDE_GROUPS:
        if members and topic in members:
            return group
    return "Other guides"


def first_summary(md: str) -> str:
    """A short one-line summary: first non-heading, non-empty prose line."""
    for line in md.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith(">") or s.startswith("|"):
            continue
        s = re.sub(r"[*`\[\]]", "", s)
        return (s[:160] + "…") if len(s) > 160 else s
    return ""


# --------------------------------------------------------------------------- #
# Main build
# --------------------------------------------------------------------------- #

def _write(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def build(doc_dir: str, out_dir: str) -> None:
    api_index = json.load(open(os.path.join(doc_dir, "api-docs.json"), encoding="utf-8"))
    resources = api_index["apis"]  # [{path: "/foo.json", description: "Foo"}]

    res_out = os.path.join(out_dir, "resources")
    guides_out = os.path.join(out_dir, "guides")

    catalog_rows: list[str] = []
    index_blocks: list[str] = []
    total_endpoints = 0
    total_models = 0

    for entry in resources:
        fname = entry["path"].lstrip("/")            # "courses.json"
        slug = os.path.splitext(fname)[0]            # "courses"
        name = entry["description"]                  # "Courses"
        fpath = os.path.join(doc_dir, fname)
        if not os.path.exists(fpath):
            print(f"  ! missing resource file: {fname}", file=sys.stderr)
            continue
        res = json.load(open(fpath, encoding="utf-8"))
        md, endpoints = render_resource(res, name)
        _write(os.path.join(res_out, f"{slug}.md"), md)

        nmodels = len(res.get("models") or {})
        total_endpoints += len(endpoints)
        total_models += nmodels
        catalog_rows.append(
            f"| [{name}](resources/{slug}.md) | {len(endpoints)} | {nmodels} | "
            f"{_cell(entry['description'])} |"
        )

        # endpoint index block
        index_blocks.append(f"\n### {name}  —  resources/{slug}.md\n")
        for ep in endpoints:
            dep = " (deprecated)" if ep["deprecated"] else ""
            index_blocks.append(
                f"`{ep['method']}` {ep['path']} — {ep['summary']} "
                f"[{ep['nickname']}]{dep}"
            )

    # ---- catalog.md ---- #
    catalog = [
        "# Canvas LMS API — Resource Catalog\n",
        f"All {len(catalog_rows)} REST API resource groups "
        f"({total_endpoints} endpoints, {total_models} models). "
        "Open a resource file for full endpoint parameters and object models.\n",
        "| Resource | Endpoints | Models | Description |",
        "| --- | --- | --- | --- |",
        *catalog_rows,
        "",
    ]
    _write(os.path.join(out_dir, "catalog.md"), "\n".join(catalog) + "\n")

    # ---- endpoints-index.md ---- #
    index = [
        "# Canvas LMS API — Endpoint Index\n",
        "One line per endpoint. `grep -i <keyword>` this file to locate an endpoint, "
        "then open the matching `resources/<slug>.md` for full parameters.\n",
        "Format: `METHOD` path — summary [nickname]\n",
        *index_blocks,
        "",
    ]
    _write(os.path.join(out_dir, "endpoints-index.md"), "\n".join(index) + "\n")

    # ---- guides + permissions (from HTML) ---- #
    n_guides, n_perms = _build_html(doc_dir, out_dir, guides_out)

    print(
        f"Built reference/ from {doc_dir}:\n"
        f"  resources : {len(catalog_rows)}\n"
        f"  endpoints : {total_endpoints}\n"
        f"  models    : {total_models}\n"
        f"  guides    : {n_guides}\n"
        f"  permissions: {n_perms}"
    )


def _build_html(doc_dir: str, out_dir: str, guides_out: str) -> tuple[int, int]:
    files = sorted(os.listdir(doc_dir))
    guide_records: list[tuple[str, str, str]] = []  # (group, topic, summary)
    perm_sections: list[tuple[str, str, str]] = []   # (title, slug, md)
    perm_overview = ""

    # Topics that are truncated duplicates or combined dumps we skip outright.
    skip_topics = {"all_resources"}

    for fname in files:
        if not fname.startswith("file.") or not fname.endswith(".html"):
            continue
        topic = fname[len("file."):-len(".html")]
        if topic in skip_topics or topic.endswith(".head"):
            continue
        raw = open(os.path.join(doc_dir, fname), encoding="utf-8").read()
        if len(raw) < 1000:
            continue
        md = guide_markdown(raw)
        if len(md.strip()) < 40:
            continue

        if topic == "permissions":
            # The RBAC overview: which permissions are account- vs course-level.
            perm_overview = md
        elif topic.startswith("permissions_"):
            perm = topic[len("permissions_"):]
            title = permission_title(md, perm)
            perm_sections.append((title, perm, md))
        else:
            # The docs landing page: give it a self-describing name so it does
            # not collide with the generated guides index (README.md).
            if topic == "README":
                topic = "overview"
            _write(os.path.join(guides_out, f"{topic}.md"), md)
            guide_records.append((classify_guide(topic), topic, first_summary(md)))

    # ---- guides/README.md ---- #
    order = [g for g, _ in GUIDE_GROUPS] + ["Other guides"]
    by_group: dict[str, list[tuple[str, str]]] = {}
    for group, topic, summary in guide_records:
        by_group.setdefault(group, []).append((topic, summary))
    lines = [
        "# Canvas LMS API — Concept Guides\n",
        "Narrative documentation extracted from the Canvas API docs. "
        "Open a guide for the full text.\n",
    ]
    for group in order:
        items = by_group.get(group)
        if not items:
            continue
        lines.append(f"\n## {group}\n")
        for topic, summary in sorted(items):
            suffix = f" — {summary}" if summary else ""
            lines.append(f"- [{topic}]({topic}.md){suffix}")
    _write(os.path.join(guides_out, "README.md"), "\n".join(lines) + "\n")

    # ---- permissions.md ---- #
    perm_sections.sort(key=lambda t: t[1])
    plines = [
        "# Canvas LMS — Account & Course Permissions (RBAC)\n",
        "Each Canvas role permission, what it enables, and its dependencies. "
        "`grep -i <permission>` to jump to one. Permission keys match the "
        "`manage_*` / `view_*` names used by the Roles API.\n",
    ]
    if perm_overview:
        body = re.sub(r"^#+\s+.*$", "", perm_overview, count=1, flags=re.M).strip()
        plines.append("## Overview: account-level vs course-level permissions\n")
        plines.append(body + "\n")
    plines.append("## Index\n")
    for title, slug, _ in perm_sections:
        plines.append(f"- **`{slug}`** — {title}")
    plines.append("\n---\n")
    for title, slug, md in perm_sections:
        # demote the page's own H1 to H2 and namespace it with the key
        body = re.sub(r"^#+\s+.*$", "", md, count=1, flags=re.M).strip()
        plines.append(f"\n## `{slug}` — {title}\n")
        plines.append(body)
    _write(os.path.join(out_dir, "permissions.md"), "\n".join(plines) + "\n")

    return len(guide_records), len(perm_sections)


def main(argv: list[str]) -> int:
    doc_dir = argv[1] if len(argv) > 1 else DEFAULT_DOC_DIR
    out_dir = argv[2] if len(argv) > 2 else DEFAULT_OUT_DIR
    if not os.path.isdir(doc_dir):
        print(f"error: doc dir not found: {doc_dir}", file=sys.stderr)
        return 1
    build(doc_dir, out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
