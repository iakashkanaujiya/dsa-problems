import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    nums = list(map(int, lines[0].split()))
    target = int(lines[1])
    result = Solution().twoSum(nums, target)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
