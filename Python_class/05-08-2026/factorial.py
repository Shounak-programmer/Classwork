def fact(i):
    if i == 0:
        return 1
    else:
        return i * fact(i - 1)

i = int(input("Enter a number to calculate its factorial: "))
if i < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = fact(i)
    print(f"The factorial of {i} is: {result}")