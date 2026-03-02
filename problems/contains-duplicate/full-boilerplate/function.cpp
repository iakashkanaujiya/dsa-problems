#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string _line0; getline(cin, _line0);
    istringstream _iss0(_line0);
    vector<int> nums; { int _v; while(_iss0 >> _v) nums.push_back(_v); }
    Solution sol;
    bool result = sol.containsDuplicate(nums);
    cout << (result ? "true" : "false") << "\n";
    return 0;
}
