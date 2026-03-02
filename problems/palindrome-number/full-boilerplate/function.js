const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const x = Number(lines[0]);
  const sol = new Solution();
  const result = sol.isPalindrome(x);
  console.log(result ? 'true' : 'false');
});
