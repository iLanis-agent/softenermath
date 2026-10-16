# Softener Math

Water softener honesty. The sticker says thirty-two thousand grains, and the salt dose was always going to have the last word. Softener Math turns hardness, rated capacity and salt dose into honest arithmetic on labeled norms.

## What it computes

- **The hardness truth** - grains per gallon read against the named bands (soft, slightly hard, moderately hard, hard, very hard) with the ppm conversion.
- **The capacity truth** - the rated grains are the max-salt figure: days between regenerations at the label and at the efficient dose (two-thirds capacity, 75 gallons per person per day, labeled norms).
- **The salt truth** - salt per regeneration times regenerations per month, as pounds and 40-pound bags.

## Boundary

Softener Math keeps labeled-norm arithmetic only. Hardness bands, the 75-gallon person-day, the two-thirds efficient dose and the ppm conversion are labeled norms, not measurements of your water, your resin or your household. Test your water with a real kit, follow the maker's capacity and salt charts over anything this page says, and ask a water professional about your plumbing.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (29 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/softenermath/
Repo: https://github.com/iLanis-agent/softenermath
