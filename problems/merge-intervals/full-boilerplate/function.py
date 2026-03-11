import sys
from typing import List

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    idx = 1
    for _ in range(t):
        _intervals_rows = []
        while idx < len(lines) and lines[idx].strip():
            _intervals_rows.append(list(map(int, lines[idx].split())))
            idx += 1
        idx += 1 # skip empty line
        intervals = _intervals_rows
        result = Solution().merge(intervals)
        for row in result:
            print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
