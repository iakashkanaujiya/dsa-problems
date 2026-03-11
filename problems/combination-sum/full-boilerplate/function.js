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
    const candidates = lines[idx++].split(' ').map(Number);
    const target = Number(lines[idx++]);
    const sol = new Solution();
    const result = sol.combinationSum(candidates, target);
    result.forEach(row => console.log(row.join(' ')));
  }
});
