package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
)

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
        s := readLine()
        result := lengthOfLongestSubstring(s)
        fmt.Println(result)
    }
}
