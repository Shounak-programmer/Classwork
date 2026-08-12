//evaluation and operation 2D 3x3 matrix
#include <iostream>
using namespace std;
int main(){
    int matrix[3][3];
    // Initialize the matrix
    cout << "Enter the elements of the 3x3 matrix:\n";
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cin >> matrix[i][j];
        }
    }
    // Display the matrix
    cout << "The entered matrix is:\n";
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }
    //even elements input
    cout << "Enter new values for even elements:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (matrix[i][j] % 2 == 0) {
                cin >> matrix[i][j];
            }
        }
    }
    // //display left diagonal elements
    // cout << "The left diagonal elements of the matrix are:\n";
    // for (int i = 0; i < 3; i++) {
    //     cout << matrix[i][i] << " ";
    // }
    // cout << endl;
    // //display right diagonal elements
    // cout << "The right diagonal elements of the matrix are:\n";
    // for (int i = 0; i < 3; i++) {
    //     cout << matrix[i][2 - i] << " ";
    // }
    // cout << endl;

    // Display the updated matrix   
    
    cout << "The updated matrix is:\n";
    for(int i = 0; i < 3; i++){
        for(int j = 0; j < 3; j++){
            cout << matrix[i][j] << " ";
        }
        cout << endl;
    }

    //Display the diagonal elements
    cout << "The diagonal elements of the matrix are:\n";
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (i == j || i + j == 2) {
                cout << matrix[i][j] << " "; // diagonal elements
            }
        }
    }
    return 0;
}
