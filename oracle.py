import math, json

def plural(n, one, many):
    return one if n == 1 else many

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def hard_truth(gpg):
    if not (gpg > 0):
        raise ValueError("the hardness must be above zero")
    if gpg < 1:
        band = "soft"
    elif gpg < 3.5:
        band = "slightly hard"
    elif gpg < 7:
        band = "moderately hard"
    elif gpg < 10.5:
        band = "hard"
    else:
        band = "very hard"
    return f"{gpg} {plural(gpg, 'grain', 'grains')} per gallon reads {band} honestly - {fixed1(gpg * 17.1)} ppm."

def cap_truth(rated, people, gpg):
    if not (rated > 0):
        raise ValueError("the grain rating must be above zero")
    if not (people > 0):
        raise ValueError("the people must be above zero")
    if not (gpg > 0):
        raise ValueError("the hardness must be above zero")
    daily = people * 75 * gpg
    label = rated / daily
    efficient = (rated * 2) / 3 / daily
    return f"A {rated}-grain rating against {people} {plural(people, 'person', 'people')} on {gpg}-grain water regenerates every {fixed1(label)} days at the label and every {fixed1(efficient)} days at the efficient dose honestly."

def salt_truth(lbs, days):
    if not (lbs > 0):
        raise ValueError("the salt per regeneration must be above zero")
    if not (days > 0):
        raise ValueError("the days between regenerations must be above zero")
    regens = tenths(30 / days)
    month = lbs * regens
    regens_text = "once a month" if regens == 1 else f"{fixed1(regens)} times a month"
    bags = tenths(month / 40)
    bags_text = "a fraction of one 40-pound bag" if bags == 0 else f"{fixed1(bags)} {plural(bags, 'bag', 'bags')} of 40"
    return f"{lbs} {plural(lbs, 'pound', 'pounds')} per regeneration {regens_text} uses {fixed1(month)} {plural(tenths(month), 'pound', 'pounds')} - {bags_text} honestly."

FNS = {"hardTruth": hard_truth, "capTruth": cap_truth, "saltTruth": salt_truth}

CASES = [
    ("hardTruth", [10]),
    ("hardTruth", [0.5]),
    ("hardTruth", [2]),
    ("hardTruth", [5]),
    ("hardTruth", [12]),
    ("hardTruth", [3.5]),
    ("hardTruth", [1]),
    ("hardTruth", [7]),
    ("hardTruth", [10.5]),
    ("hardTruth", [0]),
    ("hardTruth", [-3]),
    ("capTruth", [32000, 4, 10]),
    ("capTruth", [24000, 2, 7]),
    ("capTruth", [48000, 6, 15]),
    ("capTruth", [32000, 1, 10]),
    ("capTruth", [20000, 3, 25]),
    ("capTruth", [32000, 2.5, 10]),
    ("capTruth", [0, 4, 10]),
    ("capTruth", [32000, 0, 10]),
    ("capTruth", [32000, 4, 0]),
    ("saltTruth", [12, 10.7]),
    ("saltTruth", [6, 7.1]),
    ("saltTruth", [15, 4.7]),
    ("saltTruth", [9, 14]),
    ("saltTruth", [20, 3]),
    ("saltTruth", [1, 30]),
    ("saltTruth", [40, 30]),
    ("saltTruth", [0, 10]),
    ("saltTruth", [12, -2]),
]

out = []
for fn, args in CASES:
    rec = {"fn": fn, "args": args}
    try:
        rec["out"] = FNS[fn](*args)
    except ValueError as e:
        rec["err"] = str(e)
    out.append(rec)
    print(fn, args, "->", rec.get("out") or ("ERR: " + rec["err"]))

with open("expected.json", "w") as f:
    json.dump(out, f, indent=1)
    f.write("\n")
print(f"{len(out)} cases written")
