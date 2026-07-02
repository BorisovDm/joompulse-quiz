# 🇧🇷 Mercado Livre Quiz Games

Quiz games built on Mercado Livre product data.

## Games

**Guess the Supplier Price** — you see a product on Mercado Livre with its price and
the same product from a local Brazilian supplier; guess the supplier's price.
Landing within ±25% of the real price counts as a hit.

**Play:** https://borisovdm.github.io/local-suppliers-quiz/

**Guess the Category Tree** — you see a product from Mercado Livre; guess its full
category path level by level, picking one of 4 options at each level. 3 lives per product.

**Play:** https://borisovdm.github.io/local-suppliers-quiz/categories/

## Structure

- `index.html`, `categories/index.html` — the games, fully self-contained (data embedded)
- `template.html`, `categories/template.html` — layout and game logic; edit these, not `index.html`
- `build.py`, `categories/build.py` — rebuild `index.html` from the template and the source data

## Updating the data

- Supplier price game: put the fresh CSV at `~/Downloads/local_suppliers_quiz_data.csv`, run `python3 build.py`
- Category tree game: put the fresh JSON Lines at `~/Downloads/category_quiz_data.json`, run `python3 categories/build.py`

Then commit and push — GitHub Pages redeploys automatically.
