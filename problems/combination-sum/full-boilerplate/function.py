import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    candidates = list(map(int, lines[0].split()))
    target = int(lines[1])
    result = Solution().combinationSum(candidates, target)
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
