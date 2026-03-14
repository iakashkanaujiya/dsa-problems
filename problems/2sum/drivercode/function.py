import sys
from typing import List, Optional, Any

##USER_CODE##

def main():
    lines = sys.stdin.read().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    idx = 1
    for _ in range(t):
        nums = list(map(int, lines[idx].split())) if lines[idx] else []
        idx += 1
        target = int(lines[idx])
        idx += 1
        result = Solution().twoSum(nums, target)
        print(' '.join(map(lambda x: str(x).lower() if isinstance(x, bool) else str(x), result)))

if __name__ == '__main__':
    main()
