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
        vector<vector<int>> intervals;
        { string _row; while(getline(cin, _row) && !_row.empty()) {
            istringstream _rs(_row); vector<int> _r; int _v;
            while(_rs >> _v) _r.push_back(_v);
            intervals.push_back(_r); } }
        Solution sol;
        vector<vector<int>> result = sol.merge(intervals);
        for (auto& row : result) {
        for (int i = 0; i < (int)row.size(); i++) {
        if (i) cout << " ";
        cout << row[i];
        }
        cout << "\n";
        }
    }
    return 0;
}
