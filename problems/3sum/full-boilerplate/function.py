import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    nums = list(map(int, lines[0].split()))
    result = Solution().threeSum(nums)
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
