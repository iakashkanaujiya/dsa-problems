package main

type ListNode struct {
    Val  int
    Next *ListNode
}

func buildList(vals []int) *ListNode {
    dummy := &ListNode{}
    cur := dummy
    for _, v := range vals {
        cur.Next = &ListNode{Val: v}
        cur = cur.Next
    }
    return dummy.Next
}

func printList(head *ListNode) {
    first := true
    for head != nil {
        if !first {
            fmt.Print(" ")
        }
        fmt.Print(head.Val)
        first = false
        head = head.Next
    }
    fmt.Println()
}

func reverseList(head *ListNode) *ListNode {
    // Write your code here
}
