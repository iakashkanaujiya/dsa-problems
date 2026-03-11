import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    idx = 1
    for _ in range(t):
        nums1 = list(map(int, lines[idx].split()))
        idx += 1
        nums2 = list(map(int, lines[idx].split()))
        idx += 1
        result = Solution().findMedianSortedArrays(nums1, nums2)
        print(result)

if __name__ == "__main__":
    main()
