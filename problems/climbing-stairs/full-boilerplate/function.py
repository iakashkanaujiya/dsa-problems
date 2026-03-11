import sys

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    if not lines: return
    t = int(lines[0].strip())
    idx = 1
    for _ in range(t):
        n = int(lines[idx])
        idx += 1
        result = Solution().climbStairs(n)
        print(result)

if __name__ == "__main__":
    main()
