const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {

  ##USER_CODE##

  if (lines.length === 0) return;
  const t = Number(lines[0]);
  let idx = 1;
  for (let _i = 0; _i < t; _i++) {
    const _intervals_rows = [];
    while(idx < lines.length && lines[idx].trim() !== '') {
      _intervals_rows.push(lines[idx++].split(' ').map(Number));
    }
    idx++; // skip empty line
    const intervals = _intervals_rows;
    const sol = new Solution();
    const result = sol.merge(intervals);
    result.forEach(row => console.log(row.join(' ')));
  }
});
