#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string line;
    if (!getline(cin, line)) return 0;
    istringstream iss(line);
    int t;
    if (!(iss >> t)) return 0;
    while (t--) {
        string s; getline(cin, s);
        Solution sol;
        int result = sol.longestValidParentheses(s);
        cout << result << "\n";
    }
    return 0;
}
