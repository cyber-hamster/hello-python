"""
The Keyword cipher is identical to the Caesar Cipher with the exception that the substitution alphabet used can be
represented with a keyword.
To create a substitution alphabet from a keyword, you first write down the alphabet. Below this you write down the
keyword (omitting duplicate letters) followed by the remaining unused letters of the alphabet.
ABCDEFGHIJKLMNOPQRSTUVWXYZ
KEYWORDABCFGHIJLMNPQSTUVXZ
To encipher a plaintext message, you convert all letters from the top row to their correspondng letter on the bottom
row (A to K, B to E, etc).
These types of simple substitution ciphers can be easily cracked by using frequency analysis and some educated guessing.
http://www.braingle.com/brainteasers/codes/keyword.php
"""

c_counter = 0
index_counter = 25
temp_list = ["*"] * 26
counter = 0
new_word = ""
standard = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

revised = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

#         ['C', 'A', 'T', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'U',
#          'V', 'W', 'X', 'Y', 'Z']

keyword = input("Please enter the key word: ").upper()

# Eliminate any duplicate letters in the key word
for c in keyword:
    if c not in new_word:
        new_word += c

# Remove key word letters from the revised array
for e in revised:
    if e in keyword:
        revised[counter] = " "
    counter += 1

# Shift revised letters to the right to fill empty elements

# print(revised)
# print(temp_list)

for counter in range(25, 0, -1):
    letter = revised[counter]
    if counter >= 0:
        if letter != " ":
            temp_list[index_counter] = revised[counter]
            # print(temp_list[counter])
            # print(revised[counter])
            index_counter -= 1
# print(temp_list)

for c in new_word:
    temp_list[c_counter] = c
    c_counter += 1

# print(temp_list)

ustring = input("Enter the string to encode: ").upper()
encoded_string = ""

for c in ustring:
    element_counter = 0
    for element in standard:

        # print("element_counter is: ",element_counter)
        if c == temp_list[element_counter]:
            # print("Found a ", temp_list[element_counter], "at element number ", element_counter)
            # print(standard[element_counter])
            encoded_string += standard[element_counter]
            # print(encoded_string)
        element_counter += 1
print(temp_list)
print(standard)
print(encoded_string)