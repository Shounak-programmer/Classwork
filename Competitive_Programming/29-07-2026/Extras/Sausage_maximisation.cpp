#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

const int BITS = 41; // ai up to 1e12 < 2^40, sums/xors safely fit in 41 bits

struct Trie {
    vector<array<int,2>> ch;
    Trie() { ch.push_back({-1,-1}); }

    void insert(ll x) {
        int cur = 0;
        for (int b = BITS - 1; b >= 0; b--) {
            int bit = (x >> b) & 1;
            if (ch[cur][bit] == -1) {
                ch[cur][bit] = ch.size();
                ch.push_back({-1,-1});
            }
            cur = ch[cur][bit];
        }
    }

    ll queryMax(ll x) {
        int cur = 0;
        ll res = 0;
        for (int b = BITS - 1; b >= 0; b--) {
            int bit = (x >> b) & 1;
            int want = bit ^ 1;
            if (ch[cur][want] != -1) {
                res |= (1LL << b);
                cur = ch[cur][want];
            } else {
                cur = ch[cur][bit];
            }
        }
        return res;
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<ll> a(n);
    for (auto &x : a) cin >> x;

    vector<ll> P(n+1, 0), S(n+1, 0);
    for (int i = 0; i < n; i++) P[i+1] = P[i] ^ a[i];
    for (int j = n - 1; j >= 0; j--) S[j] = S[j+1] ^ a[j];

    Trie trie;
    ll ans = 0;
    for (int j = 0; j <= n; j++) {
        trie.insert(P[j]);              // insert P[i] for i = j (covers all i <= j so far)
        ans = max(ans, trie.queryMax(S[j]));
    }

    cout << ans << "\n";
    return 0;
}
