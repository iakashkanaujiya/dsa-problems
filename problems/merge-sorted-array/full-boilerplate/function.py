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
        m = int(lines[idx])
        idx += 1
        nums2 = list(map(int, lines[idx].split()))
        idx += 1
        n = int(lines[idx])
        idx += 1
        result = Solution().merge(nums1, m, nums2, n)
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
