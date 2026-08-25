// https://codeforces.com/contest/1861/problem/A
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n) {
    if (n < 2) return false;

    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return false;
    }

    return true;
}

void solve() {
    string s;
    cin >> s;

    // Try every subsequence.
    for (int mask = 0; mask < (1 << 9); mask++) {
        string cur;

        for (int i = 0; i < 9; i++) {
            if (mask & (1 << i))
                cur += s[i];
        }

        // We cannot delete when only two digits remain,
        // so the final sequence must have at least 2 digits.
        if (cur.size() < 2)
            continue;

        long long num = stoll(cur);

        if (isPrime(num)) {
            cout << cur << '\n';
            return;
        }
    }

    cout << -1 << '\n';
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        solve();
    }

    return 0;
}
