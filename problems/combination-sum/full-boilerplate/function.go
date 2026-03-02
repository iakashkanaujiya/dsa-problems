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
    _parts0 := strings.Fields(readLine())
    candidates := make([]int, len(_parts0))
    for _i, _s := range _parts0 { candidates[_i], _ = strconv.Atoi(_s) }
    target, _ := strconv.Atoi(readLine())
    result := combinationSum(candidates, target)
    for _, _row := range result {
        _strs := make([]string, len(_row))
        for _i, _v := range _row { _strs[_i] = strconv.Itoa(_v) }
        fmt.Println(strings.Join(_strs, " "))
    }
}
