#Write a function that finds the longest consecutive sequence of the same character in a given string.
def lcs(input_string):
    if not input_string:     # Handle empty string case
        return "", 0

    max_char = input_string[0]
    max_count = 1
    current_char = input_string[0]
    current_count = 1

    for char in input_string[1:]:
        if char == current_char:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_char = current_char
            current_char = char
            current_count = 1

    # Check last sequence
    if current_count > max_count:
        max_count = current_count
        max_char = current_char

    return max_char, max_count
a = input("Enter a string: ")
char, count = lcs(a)
print(f"The longest consecutive sequence is '{char}' with a count of {count}.")
