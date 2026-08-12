a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = input("Enter operation (+, -, *, /): ")
if c == "+":
    result = a + b
elif c == "-":
    result = a - b
elif c == "*":
    result = a * b
elif c == "/":
    result = a / b
print("The result of", a, c, b, "is", result)
