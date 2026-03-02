import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    nums1 = list(map(int, lines[0].split()))
    nums2 = list(map(int, lines[1].split()))
    result = Solution().findMedianSortedArrays(nums1, nums2)
    print(result)

if __name__ == "__main__":
    main()
