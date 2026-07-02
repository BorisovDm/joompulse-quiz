#!/usr/bin/env python3
"""Собирает categories/index.html: встраивает данные из JSON Lines в template.html."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.expanduser("~/Downloads/category_quiz_data.json")

items = []
for line in open(JSON_PATH, encoding="utf-8"):
    if not line.strip():
        continue
    r = json.loads(line)
    path = []
    for k in range(1, 8):
        name, wrong = r.get(f"l{k}_name"), r.get(f"l{k}_wrong")
        if not name:
            break
        path.append({"n": name, "w": wrong})
    if not path or not r.get("id") or not r.get("title") or not r.get("image_url"):
        continue
    items.append({"id": r["id"], "t": r["title"], "img": r["image_url"], "path": path})

data_js = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
template = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
html = template.replace("__DATA__", data_js)

out = os.path.join(HERE, "index.html")
open(out, "w", encoding="utf-8").write(html)
print(f"OK: {len(items)} товаров -> {out} ({os.path.getsize(out)//1024} KB)")
