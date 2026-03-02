import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    height = list(map(int, lines[0].split()))
    result = Solution().maxArea(height)
    print(result)

if __name__ == "__main__":
    main()
