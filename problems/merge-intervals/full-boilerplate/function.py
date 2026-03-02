import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    intervals = [list(map(int, l.split())) for l in lines[0:] if l.strip()]
    result = Solution().merge(intervals)
    for row in result:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
