#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int n; scanf("%d", &n);
    int result = climbStairs(n);
    printf("%d\n", result);
    return 0;
}
