#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n; cin >> n; cin.ignore();
    Solution sol;
    int result = sol.climbStairs(n);
    cout << result << "\n";
    return 0;
}
