# find out all the armstrong nos in the entered range
def is_armstrong(num):
    order = len(str(num))
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10
    return num == total

# Example usage:
# for i in range(1, 1000):
#     if is_armstrong(i):
#         print(i)
range_start = int(input("Enter the start of the range: "))
range_end = int(input("Enter the end of the range: "))

for i in range(range_start, range_end + 1):
    if is_armstrong(i):
        print(i)