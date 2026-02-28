const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines = [];
rl.on("line", (line) => lines.push(line.trim()));
rl.on("close", () => {
  const head = buildList(lines[0].split(" ").map(Number));

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
  console.log(vals.join(" "));
}
  ##USER_CODE##

  const result = reverseList(head);
  printList(result);
});
