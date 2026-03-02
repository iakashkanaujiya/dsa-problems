#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s; getline(cin, s);
    Solution sol;
    int result = sol.lengthOfLongestSubstring(s);
    cout << result << "\n";
    return 0;
}
