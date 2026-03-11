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
    print(' '.join(vals))



##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    idx = 1
    for _ in range(t):
        head = build_list(list(map(int, lines[idx].split())))
        idx += 1
        result = Solution().hasCycle(head)
        print("true" if result else "false")

if __name__ == "__main__":
    main()
