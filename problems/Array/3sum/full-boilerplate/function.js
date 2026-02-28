const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const nums = lines[0].split(" ").map(Number);

  ##USER_CODE##

  const result = threeSum(nums);
  result.forEach(row => console.log(row.join(" ")));
});
