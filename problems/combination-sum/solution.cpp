#include <bits/stdc++.h>
using namespace std;

class Solution {
    void dfs(int idx, int target, vector<int>& c, vector<int>& cur, vector<vector<int>>& res) {
        if (target == 0) { res.push_back(cur); return; }
        if (idx == c.size() || target < 0) return;
        cur.push_back(c[idx]);
        dfs(idx, target - c[idx], c, cur, res);
        cur.pop_back();
        dfs(idx + 1, target, c, cur, res);
    }
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> res;
        vector<int> cur;
        dfs(0, target, candidates, cur, res);
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
        vector<int> candidates; { int _v; while(_iss0 >> _v) candidates.push_back(_v); }
        int target; cin >> target; cin.ignore();
        Solution sol;
        vector<vector<int>> result = sol.combinationSum(candidates, target);
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
