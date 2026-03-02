import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    nums1 = list(map(int, lines[0].split()))
    m = int(lines[1])
    nums2 = list(map(int, lines[2].split()))
    n = int(lines[3])
    result = Solution().merge(nums1, m, nums2, n)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
