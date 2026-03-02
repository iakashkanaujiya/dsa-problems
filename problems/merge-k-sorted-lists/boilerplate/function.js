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

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
class Solution {
  mergeKLists(head) {
    // Write your code here
  }
}
