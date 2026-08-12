#wap to findout first non repeated character in a string using dictionary
def find_first_unique_char(input_string):
    char_count = {}
    
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1
        
    for char in input_string:
        if char_count[char] == 1:
            return char
            
    return None

string1 = "swiss"
string2 = "racecar"
string3 = "aabbcc"

print(f"First unique in '{string1}':", find_first_unique_char(string1))
print(f"First unique in '{string2}':", find_first_unique_char(string2))
print(f"First unique in '{string3}':", find_first_unique_char(string3))