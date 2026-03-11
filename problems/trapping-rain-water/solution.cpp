#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0, r = height.size() - 1, lmax = 0, rmax = 0, ans = 0;
        while (l < r) {
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);
            if (lmax < rmax) { ans += lmax - height[l]; l++; }
            else { ans += rmax - height[r]; r--; }
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
        vector<int> height; { int _v; while(_iss0 >> _v) height.push_back(_v); }
        Solution sol;
        int result = sol.trap(height);
        cout << result << "\n";
    }
    return 0;
}
