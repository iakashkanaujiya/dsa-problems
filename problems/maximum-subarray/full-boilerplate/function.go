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
        _parts0 := strings.Fields(readLine())
        nums := make([]int, len(_parts0))
        for _i, _s := range _parts0 { nums[_i], _ = strconv.Atoi(_s) }
        result := maxSubArray(nums)
        fmt.Println(result)
    }
}
