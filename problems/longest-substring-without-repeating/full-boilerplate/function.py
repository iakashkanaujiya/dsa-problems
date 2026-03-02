import sys

##USER_CODE##

def main():
    lines = sys.stdin.read().strip().splitlines()
    s = lines[0]
    result = Solution().lengthOfLongestSubstring(s)
    print(result)

if __name__ == "__main__":
    main()
