#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums[m] == target) return m;
            if (nums[l] <= nums[m]) {
                if (target >= nums[l] && target < nums[m]) r = m - 1;
                else l = m + 1;
            } else {
                if (target > nums[m] && target <= nums[r]) l = m + 1;
                else r = m - 1;
            }
        }
        return -1;
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
        int target; cin >> target; cin.ignore();
        Solution sol;
        int result = sol.search(nums, target);
        cout << result << "\n";
    }
    return 0;
}
