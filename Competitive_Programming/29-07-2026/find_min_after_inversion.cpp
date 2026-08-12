//codeforces problem 514A, Round 291 (Div. 2)
#include <iostream>
#include <string>
using namespace std;

int main() {
    string x;
    cin >> x;

    for (int i = 0; i < x.size(); i++) {
        int digit = x[i] - '0';
        int inverted = 9 - digit;

        // First digit cannot become 0
        if (i == 0 && inverted == 0) {
            continue;
        }

        // Use the smaller digit
        if (inverted < digit) {
            x[i] = char(inverted + '0');
        }
    }

    cout << x << endl;

    return 0;
}
