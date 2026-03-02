#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string _line0; getline(cin, _line0);
    istringstream _iss0(_line0);
    vector<int> nums1; { int _v; while(_iss0 >> _v) nums1.push_back(_v); }
    int m; cin >> m; cin.ignore();
    string _line2; getline(cin, _line2);
    istringstream _iss2(_line2);
    vector<int> nums2; { int _v; while(_iss2 >> _v) nums2.push_back(_v); }
    int n; cin >> n; cin.ignore();
    Solution sol;
    vector<int> result = sol.merge(nums1, m, nums2, n);
    for (int i = 0; i < (int)result.size(); i++) {
        if (i) cout << " ";
        cout << result[i];
    }
    cout << "\n";
    return 0;
}
