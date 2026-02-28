import sys
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" ".join(vals))


##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    head = build_list(list(map(int, lines[0].split())))
    result = reverseList(head)
    print_list(result)

if __name__ == "__main__":
    main()
