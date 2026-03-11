const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
class ListNode {
  constructor(val = 0, next = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(arr) {
  let dummy = new ListNode(0);
  let cur = dummy;
  for (const v of arr) { cur.next = new ListNode(v); cur = cur.next; }
  return dummy.next;
}

function printList(head) {
  const vals = [];
  while (head) { vals.push(head.val); head = head.next; }
  console.log(vals.join(' '));
}


  ##USER_CODE##

  if (lines.length === 0) return;
  const t = Number(lines[0]);
  let idx = 1;
  for (let _i = 0; _i < t; _i++) {
    const head = buildList(lines[idx++].split(' ').map(Number));
    const sol = new Solution();
    const result = sol.reverseList(head);
    printList(result);
  }
});
