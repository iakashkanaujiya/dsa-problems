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
    x, _ := strconv.Atoi(readLine())
    result := isPalindrome(x)
    if result { fmt.Println("true") } else { fmt.Println("false") }
}
