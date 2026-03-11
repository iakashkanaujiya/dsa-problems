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
        nums1 := make([]int, len(_parts0))
        for _i, _s := range _parts0 { nums1[_i], _ = strconv.Atoi(_s) }
        m, _ := strconv.Atoi(readLine())
        _parts2 := strings.Fields(readLine())
        nums2 := make([]int, len(_parts2))
        for _i, _s := range _parts2 { nums2[_i], _ = strconv.Atoi(_s) }
        n, _ := strconv.Atoi(readLine())
        result := merge(nums1, m, nums2, n)
        _strs := make([]string, len(result))
        for _i, _v := range result { _strs[_i] = strconv.Itoa(_v) }
        fmt.Println(strings.Join(_strs, " "))
    }
}
