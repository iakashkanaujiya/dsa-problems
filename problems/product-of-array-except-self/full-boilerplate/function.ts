const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const nums: number[] = lines[0].split(' ').map(Number);
  const sol = new Solution();
  const result = sol.productExceptSelf(nums);
  console.log(result.join(' '));
});
