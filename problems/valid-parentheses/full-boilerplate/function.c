#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    char s[100000]; scanf("%s", s);
    int result = isValid(s);
    printf("%s\n", result ? "true" : "false");
    return 0;
}
