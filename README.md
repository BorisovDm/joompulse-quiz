# 🇧🇷 Guess the Supplier Price

A quiz game: you see a product on Mercado Livre with its price and the same product
from a local Brazilian supplier — guess the supplier's price. Landing within ±25%
of the real price counts as a hit.

**Play:** https://borisovdm.github.io/supplier-quiz/

## Structure

- `index.html` — the game, fully self-contained (data embedded), just open it in a browser
- `template.html` — layout and game logic; edit this, not `index.html`
- `build.py` — rebuilds `index.html` from `template.html` and the source CSV

## Updating the data

Put the fresh CSV at `~/Downloads/local_suppliers_quiz_data.csv` and run:

```bash
python3 build.py
```

Then commit and push — GitHub Pages redeploys automatically.
