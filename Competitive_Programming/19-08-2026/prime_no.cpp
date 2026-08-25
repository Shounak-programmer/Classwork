#include <stdio.h>
#include <stdbool.h>

bool check_prime(int n, int i) {   
    if (n <= 1) {
        return false;
    }
    if (i * i > n) {
        return true;
    }
    if (n % i == 0) {
        return false;
    }
    return check_prime(n, i + 1);
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    if (check_prime(n, 2)) {
        printf("%d is a prime number.\n", n);
    } else {
        printf("%d is not a prime number.\n", n);
    }

    return 0;
}
