#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int i = m - 1, j = n - 1, k = m + n - 1;
        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) nums1[k--] = nums1[i--];
            else nums1[k--] = nums2[j--];
        }
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
        int m; cin >> m; cin.ignore();
        string _line2; getline(cin, _line2);
        istringstream _iss2(_line2);
        vector<int> nums2; { int _v; while(_iss2 >> _v) nums2.push_back(_v); }
        int n; cin >> n; cin.ignore();
        Solution sol;
        sol.merge(nums1, m, nums2, n);
        for (int i = 0; i < (int)nums1.size(); i++) {
        if (i) cout << " ";
        cout << nums1[i];
        }
        cout << "\n";
    }
    return 0;
}
