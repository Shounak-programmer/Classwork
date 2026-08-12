//codeforces problem 507A, Round 287 (Div. 2)
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<pair<int, int>> instruments;

    for (int i = 0; i < n; i++) {
        int a;
        cin >> a;
        instruments.push_back({a, i + 1});
    }

    // Sort by required days
    sort(instruments.begin(), instruments.end());

    vector<int> answer;

    for (auto [days, index] : instruments) {
        if (k >= days) {
            k -= days;
            answer.push_back(index);
        } else {
            break;
        }
    }

    cout << answer.size() << '\n';

    for (int index : answer) {
        cout << index << ' ';
    }

    cout << '\n';

    return 0;
}
