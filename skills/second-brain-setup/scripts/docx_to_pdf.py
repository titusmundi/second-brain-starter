#!/usr/bin/env python3
"""Exports 'Getting Started with Claude and Obsidian.docx' (built by build_beginner_guide.py) to a styled PDF.

Usage: python3 scripts/docx_to_pdf.py "Getting Started with Claude and Obsidian.docx" out.pdf
Needs python-docx and Google Chrome (headless print). A plain Word-to-HTML conversion loses the headings,
so this reads the document structure (title, headings, numbered steps, callout boxes, tables) and prints clean HTML.
"""
import docx, html, re, subprocess, sys, tempfile, os
from docx.text.paragraph import Paragraph
from docx.table import Table

CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CSS = """
@page{size:Letter;margin:0.9in 1in}
body{font-family:Georgia,'Times New Roman',serif;color:#1a1a1a;font-size:11.5pt;line-height:1.5}
h1.title{font-family:Helvetica,Arial,sans-serif;font-size:26pt;margin:0 0 4pt}
.subtitle{font-family:Helvetica,Arial,sans-serif;font-size:13pt;color:#555;margin:0 0 18pt}
h2{font-family:Helvetica,Arial,sans-serif;font-size:16pt;margin:26pt 0 8pt;border-bottom:1.5px solid #5B3A8E;padding-bottom:3pt;page-break-after:avoid}
h3{font-family:Helvetica,Arial,sans-serif;font-size:12.5pt;margin:16pt 0 6pt;color:#5B3A8E;page-break-after:avoid}
p{margin:0 0 9pt}
.step{display:flex;gap:10pt;margin:0 0 8pt;page-break-inside:avoid}
.step .n{font-family:Helvetica,Arial,sans-serif;font-weight:700;color:#5B3A8E;min-width:16pt}
.callout{border-left:4px solid #5B3A8E;background:#f4f0fa;padding:9pt 12pt;margin:12pt 0;page-break-inside:avoid}
.callout .ct{font-family:Helvetica,Arial,sans-serif;font-weight:700;color:#5B3A8E;margin-bottom:4pt}
.callout p{margin:0 0 5pt;font-size:11pt}
ul{margin:0 0 9pt 18pt;padding:0} li{margin-bottom:5pt}
table.gloss{border-collapse:collapse;width:100%;margin:8pt 0;font-size:10.5pt}
table.gloss th{background:#5B3A8E;color:#fff;text-align:left;padding:5pt 8pt;font-family:Helvetica,Arial,sans-serif}
table.gloss td{border-bottom:1px solid #ddd;padding:5pt 8pt;vertical-align:top}
"""
def runs_html(p):
    out = ""
    for r in p.runs:
        t = html.escape(r.text)
        if not t: continue
        if r.bold: t = "<strong>%s</strong>" % t
        if r.italic: t = "<em>%s</em>" % t
        out += t
    return out
def para_html(p):
    st, txt = p.style.name, p.text.strip()
    if not txt: return ""
    if st == "Title": return "<h1 class='title'>%s</h1>" % html.escape(txt)
    if st == "Heading 1": return "<h2>%s</h2>" % html.escape(txt)
    if st == "Heading 2": return "<h3>%s</h3>" % html.escape(txt)
    if st == "List Bullet": return "<ul><li>%s</li></ul>" % runs_html(p)
    m = re.match(r"^(\d+)\.\t(.*)$", p.text, re.S)
    if m:
        h = re.sub(r"^(<[^>]+>)*\d+\.\s*(</[^>]+>)*\s*", "", runs_html(p))
        return "<div class='step'><span class='n'>%s</span><div>%s</div></div>" % (m.group(1), h)
    return "<p>%s</p>" % runs_html(p)
def build(docx_path):
    d = docx.Document(docx_path); body = []
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            h = para_html(Paragraph(el, d))
            if h:
                if h.startswith("<p>") and len(body) == 1 and "title" in body[0]:
                    h = h.replace("<p>", "<p class='subtitle'>", 1)
                body.append(h)
        elif tag == 'tbl':
            t = Table(el, d)
            if len(t.rows) == 1:
                ps = [Paragraph(x, d) for x in t.rows[0].cells[0]._tc.iterchildren() if x.tag.endswith('}p')]
                ps = [p for p in ps if p.text.strip()]
                body.append("<div class='callout'><div class='ct'>%s</div>%s</div>" % (
                    html.escape(ps[0].text.strip()), "".join("<p>%s</p>" % runs_html(p) for p in ps[1:])))
            else:
                rows = "".join("<tr>" + "".join("<%s>%s</%s>" % ("th" if i == 0 else "td", html.escape(c.text.strip()), "th" if i == 0 else "td") for c in r.cells) + "</tr>" for i, r in enumerate(t.rows))
                body.append("<table class='gloss'>%s</table>" % rows)
    return "<!doctype html><meta charset='utf-8'><style>%s</style>%s" % (CSS, "\n".join(body).replace("</ul>\n<ul>", "\n"))
if __name__ == "__main__":
    src, out = sys.argv[1], os.path.abspath(sys.argv[2])
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(build(src)); tmp = f.name
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--print-to-pdf=" + out, "file://" + tmp], check=True, capture_output=True)
    print("wrote", out)
