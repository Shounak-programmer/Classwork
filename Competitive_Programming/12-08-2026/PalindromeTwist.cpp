//Codeforces problem 1027A, Round 49 (Div. 2)

#include <bits/stdc++.h>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n;
        string s;

        cin >> n;
        cin >> s;

        bool possible = true;

        for (int i = 0; i < n / 2; i++) {
            int diff = abs(s[i] - s[n - 1 - i]);

            if (diff != 0 && diff != 2) {
                possible = false;
                break;
            }
        }

        cout << (possible ? "YES" : "NO") << '\n';
    }

    return 0;
}
