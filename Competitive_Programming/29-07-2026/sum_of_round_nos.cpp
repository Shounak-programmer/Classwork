// Codeforces Problem 1352A, Round 640 (Div. 4)
#include <iostream>
using namespace std;

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        int temp = n;
        int count = 0;

        // Count non-zero digits
        while (temp > 0) {
            if (temp % 10 != 0) {
                count++;
            }
            temp /= 10;
        }

        cout << count << endl;

        // Generate round numbers
        int place = 1;

        while (n > 0) {
            int digit = n % 10;

            if (digit != 0) {
                cout << digit * place << " ";
            }

            n /= 10;
            place *= 10;
        }

        cout << endl;
    }

    return 0;
}
