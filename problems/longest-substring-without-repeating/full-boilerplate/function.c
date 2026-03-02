#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    char s[100000]; scanf("%s", s);
    int result = lengthOfLongestSubstring(s);
    printf("%d\n", result);
    return 0;
}
