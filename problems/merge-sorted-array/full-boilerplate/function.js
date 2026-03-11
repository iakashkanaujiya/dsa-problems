const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  if (lines.length === 0) return;
  const t = Number(lines[0]);
  let idx = 1;
  for (let _i = 0; _i < t; _i++) {
    const nums1 = lines[idx++].split(' ').map(Number);
    const m = Number(lines[idx++]);
    const nums2 = lines[idx++].split(' ').map(Number);
    const n = Number(lines[idx++]);
    const sol = new Solution();
    const result = sol.merge(nums1, m, nums2, n);
    console.log(result.join(' '));
  }
});
