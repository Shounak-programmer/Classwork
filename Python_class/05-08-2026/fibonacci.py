def fibonacci(n):
    """Return the Fibonacci series upto n terms."""
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_series = [0, 1]
        for i in range(2, n):
            fib_series.append(fib_series[-1] + fib_series[-2])
        return fib_series
n = input("Enter the number of terms for the Fibonacci series: ")
n = int(n)
try:
    result = fibonacci(n)
    print(f"The Fibonacci series up to {n} terms is: {result}")
except ValueError as e:
    print(f"Error: {e}")