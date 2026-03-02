const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const nums1: number[] = lines[0].split(' ').map(Number);
  const nums2: number[] = lines[1].split(' ').map(Number);
  const sol = new Solution();
  const result = sol.findMedianSortedArrays(nums1, nums2);
  console.log(result);
});
