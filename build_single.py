#!/usr/bin/env python3
"""Bygg ein einfils-versjon av sida med alle bileta innbakte som data-URI-ar.

Bruk:  python3 build_single.py
Skriv: dist/hon1000-innforing.html  (heil HTML-side, kan opnast direkte)
       dist/artifact.html           (utan doctype/html/head/body, for Claude Artifacts)
"""
import base64
import mimetypes
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "index.html")
DIST = os.path.join(HERE, "dist")
os.makedirs(DIST, exist_ok=True)

with open(SRC, encoding="utf-8") as f:
    html = f.read()


def inline(match):
    path = match.group(1)
    full = os.path.join(HERE, path)
    mime = mimetypes.guess_type(full)[0] or "application/octet-stream"
    with open(full, "rb") as fh:
        data = base64.b64encode(fh.read()).decode("ascii")
    return 'src="data:%s;base64,%s"' % (mime, data)


single = re.sub(r'src="(img/[^"]+)"', inline, html)

with open(os.path.join(DIST, "hon1000-innforing.html"), "w", encoding="utf-8") as f:
    f.write(single)

head = re.search(r"<head>(.*?)</head>", single, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", single, re.S).group(1)
fragment = head.strip() + "\n" + body.strip() + "\n"
with open(os.path.join(DIST, "artifact.html"), "w", encoding="utf-8") as f:
    f.write(fragment)

for name in ("hon1000-innforing.html", "artifact.html"):
    size = os.path.getsize(os.path.join(DIST, name))
    print("%-24s %.1f MB" % (name, size / 1e6))
