# Program to find the ASCII value of the given character

# Change this value for a different result
# c = 'p'

# Uncomment to take character from user
# c = input("Enter a character: ")

# print("The ASCII value of '" + c + "' is",ord(c))

# // Commented code above is from the Web. You can try it if you like. My code is below.

final_string = ""
text_string = "Cheers"
for c in "Cheers":
    ascii_string = ord(c)
    final_string = final_string + " " + str(ascii_string)

print(final_string)
