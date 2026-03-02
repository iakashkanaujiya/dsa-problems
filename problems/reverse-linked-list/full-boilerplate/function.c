#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct ListNode {
    int val;
    struct ListNode* next;
};

struct ListNode* buildList(int* vals, int n) {
    struct ListNode dummy;
    dummy.next = NULL;
    struct ListNode* cur = &dummy;
    for (int i = 0; i < n; i++) {
        cur->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        cur->next->val = vals[i];
        cur->next->next = NULL;
        cur = cur->next;
    }
    return dummy.next;
}

void printList(struct ListNode* head) {
    int first = 1;
    while (head) {
        if (!first) printf(" ");
        printf("%d", head->val);
        first = 0;
        head = head->next;
    }
    printf("\n");
}

##USER_CODE##

int main() {
    int _vals0[100000]; int _n0 = 0;
    { char _buf0[1000000]; fgets(_buf0, sizeof(_buf0), stdin);
      char* _tok = strtok(_buf0, " \n");
      while (_tok) { _vals0[_n0++] = atoi(_tok); _tok = strtok(NULL, " \n"); } }
    struct ListNode* head = buildList(_vals0, _n0);
    struct ListNode* result = reverseList(head);
    printList(result);
    return 0;
}
