#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int nums[100000]; int nums_n = 0;
    { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
      char* _tok = strtok(_buf0, " \n");
      while (_tok) { nums[nums_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    int result = singleNumber(nums, nums_n);
    printf("%d\n", result);
    return 0;
}
