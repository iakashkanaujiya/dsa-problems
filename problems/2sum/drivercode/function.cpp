#include <bits/stdc++.h>
using namespace std;

##USER_CODE##

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string line;
    if (!getline(cin, line)) return 0;
    istringstream iss(line);
    int t;
    if (!(iss >> t)) return 0;
    while (t--)
    {
        getline(cin, line);
        iss.clear();
        iss.str(line);

        vector<int> nums;
        int _nums_item;
        while (iss >> _nums_item) {
            nums.push_back(_nums_item);
        }
        getline(cin, line);
        iss.clear();
        iss.str(line);

        int target;
        if (!(iss >> target)) target = 0;
        Solution sol;
        vector<int> result = sol.twoSum(nums, target);

        for (int i = 0; i < result.size(); i++) {
            if (i > 0) cout << " ";
            cout << result[i];
        }
        cout << "\n";
    }
    return 0;
}
