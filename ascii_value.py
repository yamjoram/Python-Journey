
Questions : Write a program to print ASCII value of a character.


character = input("Enter the character")

def get_ascii_value(char):
    if len(char) == 1:
        return ord(char)
    else: 
        return None
    
ascii_value = get_ascii_value(character)

if ascii_value is not None:
    print(f" the ascii value of {character} is {ascii_value} ")
else:
    print("invalid")
