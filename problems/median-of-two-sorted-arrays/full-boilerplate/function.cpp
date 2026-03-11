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
