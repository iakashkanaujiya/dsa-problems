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

struct ListNode* reverseList(struct ListNode* head) {
    /* Write your code here */
}
