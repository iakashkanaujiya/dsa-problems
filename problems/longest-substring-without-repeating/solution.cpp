#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        vector<int> pos(256, -1);
        int ans = 0, l = 0;
        for (int r = 0; r < s.size(); r++) {
            if (pos[s[r]] != -1) l = max(l, pos[s[r]] + 1);
            ans = max(ans, r - l + 1);
            pos[s[r]] = r;
        }
        return ans;
    }
};

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
        int result = sol.lengthOfLongestSubstring(s);
        cout << result << "\n";
    }
    return 0;
}
