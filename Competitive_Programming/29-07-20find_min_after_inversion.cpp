//codeforces problem 514A, Round 291 (Div. 2)
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() {
    string x;

    cout << "Enter a 4 digit no: ";
    cin >> x;

    string ans = "";

    for (int i = 0; i < x.size(); i++) {
        int digit = x[i] - '0';
        int inverted = 9 - digit;

        if (i == 0) {
            // First digit cannot become 0
            if (inverted != 0 && inverted < digit)
                digit = inverted;
        } else {
            // Choose the smaller value
            digit = min(digit, inverted);
        }

        ans += char(digit + '0');
    }

    cout << "Answer: " << ans << endl;

    return 0;
}
