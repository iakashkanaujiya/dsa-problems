const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const nums: number[] = lines[0].split(' ').map(Number);
  const target: number = Number(lines[1]);
  const sol = new Solution();
  const result = sol.twoSum(nums, target);
  console.log(result.join(' '));
});
