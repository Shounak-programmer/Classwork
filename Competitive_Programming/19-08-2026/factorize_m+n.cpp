//https://codeforces.com/problemset/problem/1740/A

// int main() {
    
//     if (ones > 0) {
//         cout << "1 ";
//         ones--;
//     }

//     while (twos > 0) {
//         cout << "2 ";
//         twos--;
//     }

//     while (ones > 0) {
//         cout << "1 ";
//         ones--;
//     }

//     cout << "\n";

//     return 0;
// }
#include <bits/stdc++.h>
using namespace std;

int main() {
    int ones, twos;
    cin >> ones >> twos;

    if (ones > 0) {
        cout << "1 ";
        ones--;
    }

    while (twos > 0) {
        cout << "2 ";
        twos--;
    }

    while (ones > 0) {
        cout << "1 ";
        ones--;
    }

    cout << "\n";

    return 0;
}
