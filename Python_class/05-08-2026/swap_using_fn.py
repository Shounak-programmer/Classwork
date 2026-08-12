'''swap 2 numbers using function'''
def swap(a,b):
    temp = a
    a = b
    b = temp
    return a, b

a = int(input("a = "))
b = int(input("b = "))
a, b = swap(a, b)
print("After swapping: a =", a, "b =", b)
