const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const candidates = lines[0].split(' ').map(Number);
  const target = Number(lines[1]);
  const sol = new Solution();
  const result = sol.combinationSum(candidates, target);
  result.forEach(row => console.log(row.join(' ')));
});
