#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    int nums1[100000]; int nums1_n = 0;
    { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
      char* _tok = strtok(_buf0, " \n");
      while (_tok) { nums1[nums1_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    int m; scanf("%d", &m);
    int nums2[100000]; int nums2_n = 0;
    { char _buf2[1000000]; fgets(_buf2, sizeof(_buf2), stdin);
      char* _tok = strtok(_buf2, " \n");
      while (_tok) { nums2[nums2_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    int n; scanf("%d", &n);
    int* result = merge(nums1, nums1_n, m, nums2, nums2_n, n);
    for (int i = 0; i < result_n; i++) {
        if (i) printf(" ");
        printf("%d", result[i]);
    }
    printf("\n");
    return 0;
}
