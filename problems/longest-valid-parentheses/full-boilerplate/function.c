#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    char t_buf[256];
    if (!fgets(t_buf, sizeof(t_buf), stdin)) return 0;
    int t = atoi(t_buf);
    while (t--) {
        char s[100000]; scanf("%s", s);
        int _c; while((_c = getchar()) != '\n' && _c != EOF);
        int result = longestValidParentheses(s);
        printf("%d\n", result);
    }
    return 0;
}
