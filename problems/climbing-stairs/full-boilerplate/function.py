import sys

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    n = int(lines[0])
    result = Solution().climbStairs(n)
    print(result)

if __name__ == "__main__":
    main()
