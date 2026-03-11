const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  if (lines.length === 0) return;
  const t: number = Number(lines[0]);
  let idx = 1;
  for (let _i = 0; _i < t; _i++) {
    const nums: number[] = lines[idx++].split(' ').map(Number);
    const sol = new Solution();
    const result = sol.maxSubArray(nums);
    console.log(result);
  }
});
