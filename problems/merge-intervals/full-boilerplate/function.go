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
        var intervals [][]int
        for {
            _line := readLine()
            if _line == "" { break }
            _ps := strings.Fields(_line)
            _row := make([]int, len(_ps))
            for _i, _s := range _ps { _row[_i], _ = strconv.Atoi(_s) }
            intervals = append(intervals, _row)
        }
        result := merge(intervals)
        for _, _row := range result {
            _strs := make([]string, len(_row))
            for _i, _v := range _row { _strs[_i] = strconv.Itoa(_v) }
            fmt.Println(strings.Join(_strs, " "))
        }
    }
}
