package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

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

##USER_CODE##

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Buffer(make([]byte, 1024*1024), 1024*1024)
    scanner.Split(bufio.ScanLines)
    readLine := func() string {
        scanner.Scan()
        return strings.TrimSpace(scanner.Text())
    }
    tStr := readLine()
    if tStr == "" { return }
    t, _ := strconv.Atoi(tStr)
    for i := 0; i < t; i++ {
        _parts0 := strings.Fields(readLine())
        _vals0 := make([]int, len(_parts0))
        for _i, _s := range _parts0 { _vals0[_i], _ = strconv.Atoi(_s) }
        head := buildList(_vals0)
        result := hasCycle(head)
        if result { fmt.Println("true") } else { fmt.Println("false") }
    }
}
