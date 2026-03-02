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
    prices := make([]int, len(_parts0))
    for _i, _s := range _parts0 { prices[_i], _ = strconv.Atoi(_s) }
    result := maxProfit(prices)
    fmt.Println(result)
}
