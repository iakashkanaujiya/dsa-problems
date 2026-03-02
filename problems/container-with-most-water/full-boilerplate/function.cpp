#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string _line0; getline(cin, _line0);
    istringstream _iss0(_line0);
    vector<int> height; { int _v; while(_iss0 >> _v) height.push_back(_v); }
    Solution sol;
    int result = sol.maxArea(height);
    cout << result << "\n";
    return 0;
}
