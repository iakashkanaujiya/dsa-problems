import sys

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    x = int(lines[0])
    result = Solution().isPalindrome(x)
    print("true" if result else "false")

if __name__ == "__main__":
    main()
