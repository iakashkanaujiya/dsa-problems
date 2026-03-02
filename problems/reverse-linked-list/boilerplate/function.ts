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

class Solution {
  reverseList(head: ListNode | null): ListNode | null {
    // Write your code here
  }
}
