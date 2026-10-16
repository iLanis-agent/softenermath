// Softener Math engine - hypothetical arithmetic on labeled norms only.
// Hardness bands, per-person gallons, efficient-dose ratios and ppm
// conversion are labeled norms, not measurements of your water or resin.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function fixed1(x) { return tenths(x).toFixed(1); }

function hardTruth(gpg) {
  if (!(gpg > 0)) throw new Error("the hardness must be above zero");
  let band;
  if (gpg < 1) band = "soft";
  else if (gpg < 3.5) band = "slightly hard";
  else if (gpg < 7) band = "moderately hard";
  else if (gpg < 10.5) band = "hard";
  else band = "very hard";
  return `${gpg} ${plural(gpg, "grain", "grains")} per gallon reads ${band} honestly - ${fixed1(gpg * 17.1)} ppm.`;
}

function capTruth(rated, people, gpg) {
  if (!(rated > 0)) throw new Error("the grain rating must be above zero");
  if (!(people > 0)) throw new Error("the people must be above zero");
  if (!(gpg > 0)) throw new Error("the hardness must be above zero");
  const daily = people * 75 * gpg; // labeled norm: 75 gallons per person per day
  const label = rated / daily;
  const efficient = (rated * 2) / 3 / daily; // labeled norm: two-thirds capacity at the efficient salt dose
  return `A ${rated}-grain rating against ${people} ${plural(people, "person", "people")} on ${gpg}-grain water regenerates every ${fixed1(label)} days at the label and every ${fixed1(efficient)} days at the efficient dose honestly.`;
}

function saltTruth(lbs, days) {
  if (!(lbs > 0)) throw new Error("the salt per regeneration must be above zero");
  if (!(days > 0)) throw new Error("the days between regenerations must be above zero");
  const regens = tenths(30 / days); // rounded figure the verdict judges
  const month = lbs * regens;
  const regensText = regens === 1 ? "once a month" : `${fixed1(regens)} times a month`;
  const bags = tenths(month / 40);
  const bagsText = bags === 0 ? "a fraction of one 40-pound bag" : `${fixed1(bags)} ${plural(bags, "bag", "bags")} of 40`;
  return `${lbs} ${plural(lbs, "pound", "pounds")} per regeneration ${regensText} uses ${fixed1(month)} ${plural(tenths(month), "pound", "pounds")} - ${bagsText} honestly.`;
}

if (typeof module !== "undefined") {
  module.exports = { hardTruth, capTruth, saltTruth };
}
