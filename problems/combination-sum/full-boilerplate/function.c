#include <stdio.h>
#include <stdlib.h>
#include <string.h>

##USER_CODE##

int main() {
    char t_buf[256];
    if (!fgets(t_buf, sizeof(t_buf), stdin)) return 0;
    int t = atoi(t_buf);
    while (t--) {
        int candidates[100000]; int candidates_n = 0;
        { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
          char* _tok = strtok(_buf0, " \n");
          while (_tok) { candidates[candidates_n++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
        int target; scanf("%d", &target);
        int _c; while((_c = getchar()) != '\n' && _c != EOF);
        int** result = combinationSum(candidates, candidates_n, target);
        printf("%d\n", result);
    }
    return 0;
}
