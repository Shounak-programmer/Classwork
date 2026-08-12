// Codeforces Problem 1352A, Round 640 (Div. 4)
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;

    cout << "Enter the number: ";
    cin >> n;

    vector<int> placeValues = {1000, 100, 10, 1};
    vector<int> parts;

    for (int place : placeValues) {
        int digit = n / place;

        if (digit != 0) {
            parts.push_back(digit * place);
            n = n % place;
        }
    }

    for (int i = 0; i < parts.size(); i++) {
        cout << parts[i];

        if (i != parts.size() - 1)
            cout << " + ";
    }

    cout << endl;

    return 0;
}
