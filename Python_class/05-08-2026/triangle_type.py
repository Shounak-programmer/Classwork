'''
user will enter the lengths of the three sides of a triangle and the program will determine whether the triangle is equilateral, isosceles, or scalene.
'''
a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Invalid input. The lengths of the sides must be positive numbers.")
else: 
    if a + b <= c or a + c <= b or b + c <= a:
        print("Invalid input. The lengths of the sides do not form a triangle.")
    else:
       if a == b == c:
        print("The triangle is equilateral.")
       elif a == b or b == c or a == c:
        print("The triangle is isosceles.")
       else:
        print("The triangle is scalene.")