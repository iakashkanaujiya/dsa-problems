#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        int rp = 1;
        for (int i = 0; i < n; i++) { res[i] *= rp; rp *= nums[i]; }
        rp = 1;
        for (int i = n - 1; i >= 0; i--) { res[i] *= rp; rp *= nums[i]; }
        return res;
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
        vector<int> nums; { int _v; while(_iss0 >> _v) nums.push_back(_v); }
        Solution sol;
        vector<int> result = sol.productExceptSelf(nums);
        for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
