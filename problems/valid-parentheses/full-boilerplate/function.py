import sys

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    s = lines[0]
    result = Solution().isValid(s)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
