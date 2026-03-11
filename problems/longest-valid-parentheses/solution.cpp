#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int longestValidParentheses(string s) {
        int ans = 0;
        vector<int> st;
        st.push_back(-1);
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') st.push_back(i);
            else {
                st.pop_back();
                if (st.empty()) st.push_back(i);
                else ans = max(ans, i - st.back());
            }
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
        int result = sol.longestValidParentheses(s);
        cout << result << "\n";
    }
    return 0;
}
