#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int mn = 1e9, ans = 0;
        for (int p : prices) {
            ans = max(ans, p - mn);
            mn = min(mn, p);
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
        string _line0; getline(cin, _line0);
        istringstream _iss0(_line0);
        vector<int> prices; { int _v; while(_iss0 >> _v) prices.push_back(_v); }
        Solution sol;
        int result = sol.maxProfit(prices);
        cout << result << "\n";
    }
    return 0;
}
