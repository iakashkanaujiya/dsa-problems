#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) return findMedianSortedArrays(nums2, nums1);
        int n = nums1.size(), m = nums2.size();
        int l = 0, r = n;
        while (l <= r) {
            int p1 = (l + r) / 2;
            int p2 = (n + m + 1) / 2 - p1;
            int mx1 = (p1 == 0) ? -1e9 : nums1[p1 - 1];
            int mn1 = (p1 == n) ? 1e9 : nums1[p1];
            int mx2 = (p2 == 0) ? -1e9 : nums2[p2 - 1];
            int mn2 = (p2 == m) ? 1e9 : nums2[p2];
            if (mx1 <= mn2 && mx2 <= mn1) {
                if ((n + m) % 2 == 0) return (max(mx1, mx2) + min(mn1, mn2)) / 2.0;
                else return max(mx1, mx2);
            } else if (mx1 > mn2) {
                r = p1 - 1;
            } else {
                l = p1 + 1;
            }
        }
        return 0;
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
        vector<int> nums1; { int _v; while(_iss0 >> _v) nums1.push_back(_v); }
        string _line1; getline(cin, _line1);
        istringstream _iss1(_line1);
        vector<int> nums2; { int _v; while(_iss1 >> _v) nums2.push_back(_v); }
        Solution sol;
        double result = sol.findMedianSortedArrays(nums1, nums2);
        cout << result << "\n";
    }
    return 0;
}
