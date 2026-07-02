#!/usr/bin/env python3
"""Собирает index.html: встраивает данные из CSV в template.html."""
import csv, json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.expanduser("~/Downloads/local_suppliers_quiz_data.csv")

raw = open(CSV_PATH, encoding="utf-8", errors="replace").read()
# в исходном CSV встречаются управляющие символы на месте потерянных букв — убираем
raw = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f�]", "", raw)
rows = list(csv.DictReader(raw.splitlines()))

items = []
for r in rows:
    try:
        items.append({
            "id": r["supplier_item_id"].strip(),
            "si": r["supplier_image_url"].strip(),
            "st": r["supplier_title"].strip(),
            "sp": round(float(r["supplier_price"]), 2),
            "mi": r["mlb_image_url"].strip(),
            "mt": r["mlb_title"].strip(),
            "mp": round(float(r["mlb_price"]), 2),
            "c": r["mlb_category"].strip(),
        })
    except (KeyError, ValueError):
        continue

data_js = json.dumps(items, ensure_ascii=False, separators=(",", ":"))
template = open(os.path.join(HERE, "template.html"), encoding="utf-8").read()
html = template.replace("__DATA__", data_js)

out = os.path.join(HERE, "index.html")
open(out, "w", encoding="utf-8").write(html)
print(f"OK: {len(items)} товаров -> {out} ({os.path.getsize(out)//1024} KB)")
