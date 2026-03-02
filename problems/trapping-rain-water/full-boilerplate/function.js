const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const height = lines[0].split(' ').map(Number);
  const sol = new Solution();
  const result = sol.trap(height);
  console.log(result);
});
