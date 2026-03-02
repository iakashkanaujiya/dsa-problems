#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int** intervals; scanf("%d", &intervals);
    int** result = merge(intervals);
    printf("%d\n", result);
    return 0;
}
