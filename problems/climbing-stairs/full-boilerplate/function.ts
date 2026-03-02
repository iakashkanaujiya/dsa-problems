const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const n: number = Number(lines[0]);
  const sol = new Solution();
  const result = sol.climbStairs(n);
  console.log(result);
});
