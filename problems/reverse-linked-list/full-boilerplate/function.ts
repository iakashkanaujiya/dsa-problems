const readline = require("readline");
const rl = readline.createInterface({ input: process.stdin });
const lines: string[] = [];
rl.on("line", (line: string) => lines.push(line.trim()));
rl.on("close", () => {
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val: number = 0, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(arr: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let cur = dummy;
  for (const v of arr) { cur.next = new ListNode(v); cur = cur.next; }
  return dummy.next;
}

function printList(head: ListNode | null): void {
  const vals: number[] = [];
  while (head) { vals.push(head.val); head = head.next; }
  console.log(vals.join(' '));
}


  ##USER_CODE##

  if (lines.length === 0) return;
  const t: number = Number(lines[0]);
  let idx = 1;
  for (let _i = 0; _i < t; _i++) {
    const head: ListNode | null = buildList(lines[idx++].split(' ').map(Number));
    const sol = new Solution();
    const result = sol.reverseList(head);
    printList(result);
  }
});
