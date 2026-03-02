#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int height[100000]; int height_n = 0;
    { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
      char* _tok = strtok(_buf0, " \n");
      while (_tok) { height[height_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    int result = maxArea(height, height_n);
    printf("%d\n", result);
    return 0;
}
