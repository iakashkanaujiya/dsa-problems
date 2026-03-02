const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const nums1 = lines[0].split(' ').map(Number);
  const nums2 = lines[1].split(' ').map(Number);
  const sol = new Solution();
  const result = sol.findMedianSortedArrays(nums1, nums2);
  console.log(result);
});
