//codeforces problem 1244B, round 592 (Div. 2)

#include <bits/stdc++.h>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        string s;

        cin >> n >> s;

        int ans = n;  // At least one entire floor can always be visited.

        for (int i = 0; i < n; i++) {
            if (s[i] == '1') {
                // i is 0-based, so position is i + 1.
                int left = 2 * (i + 1);
                int right = 2 * (n - i);

                ans = max(ans, max(left, right));
            }
        }

        cout << ans << '\n';
    }

    return 0;
}
