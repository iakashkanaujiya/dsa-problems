const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  const intervals: number[][] = lines.slice(0).filter(l => l !== '').map(l => l.split(' ').map(Number));
  const sol = new Solution();
  const result = sol.merge(intervals);
  result.forEach(row => console.log(row.join(' ')));
});
