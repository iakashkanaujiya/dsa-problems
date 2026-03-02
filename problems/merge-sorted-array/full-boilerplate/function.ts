const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const nums1: number[] = lines[0].split(' ').map(Number);
  const m: number = Number(lines[1]);
  const nums2: number[] = lines[2].split(' ').map(Number);
  const n: number = Number(lines[3]);
  const sol = new Solution();
  const result = sol.merge(nums1, m, nums2, n);
  console.log(result.join(' '));
});
