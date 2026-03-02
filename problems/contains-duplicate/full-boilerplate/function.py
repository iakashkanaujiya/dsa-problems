import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    nums = list(map(int, lines[0].split()))
    result = Solution().containsDuplicate(nums)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
