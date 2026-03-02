#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s; getline(cin, s);
    Solution sol;
    bool result = sol.isValid(s);
    cout << (result ? "true" : "false") << "\n";
    return 0;
}
