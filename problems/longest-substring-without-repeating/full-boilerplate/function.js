const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const s = lines[0];
  const sol = new Solution();
  const result = sol.lengthOfLongestSubstring(s);
  console.log(result);
});
