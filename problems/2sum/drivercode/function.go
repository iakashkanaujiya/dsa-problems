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
        _nums_parts := strings.Fields(readLine())
        nums := make([]int, len(_nums_parts))
        for _i, _s := range _nums_parts { nums[_i], _ = strconv.Atoi(_s) }
        target, _ := strconv.Atoi(readLine())
        result := twoSum(nums, target)
        _result_strs := make([]string, len(result))
        for _i, _v := range result { _result_strs[_i] = fmt.Sprint(_v) }
        fmt.Println(strings.Join(_result_strs, " "))
    }
}
