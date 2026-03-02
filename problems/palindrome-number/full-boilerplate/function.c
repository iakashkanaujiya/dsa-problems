#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int x; scanf("%d", &x);
    int result = isPalindrome(x);
    printf("%s\n", result ? "true" : "false");
    return 0;
}
