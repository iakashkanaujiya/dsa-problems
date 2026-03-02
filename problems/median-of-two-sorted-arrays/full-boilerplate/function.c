#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int nums1[100000]; int nums1_n = 0;
    { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
      char* _tok = strtok(_buf0, " \n");
      while (_tok) { nums1[nums1_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    int nums2[100000]; int nums2_n = 0;
    { char _buf1[1000000]; fgets(_buf1, sizeof(_buf1), stdin);
      char* _tok = strtok(_buf1, " \n");
      while (_tok) { nums2[nums2_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    double result = findMedianSortedArrays(nums1, nums1_n, nums2, nums2_n);
    printf("%d\n", result);
    return 0;
}
