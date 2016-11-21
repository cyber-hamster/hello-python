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

def parse_keyword(keyword):
    # Eliminate any duplicate letters in the key word
    new_word = ""
    for c in keyword:
        if c not in new_word:
            new_word += c
    return new_word

def remove_letters(revised):
    # Remove key word letters from the revised array
    counter = 0
    for e in revised:
        if e in keyword:
            revised[counter] = " "
        counter += 1
    return revised

def shift_revised_elements_right():
    # Shift revised letters to the right to fill empty elements
    index_counter = 25
    for counter in range(25, 0, -1):
        letter = revised[counter]
        if counter >= 0:
            if letter != " ":
                temp_list[index_counter] = revised[counter]
                index_counter -= 1

def insert_keyword_letters(revised):
    # Insert letters from the keyword into the first elements of the list
    c_counter = 0
    for c in no_duplicate_letters:
        temp_list[c_counter] = c
        c_counter += 1

def encode_the_message(ustring):
    encoded_string = ""
    for c in ustring:
        element_counter = 0
        if c == " ":
            encoded_string += " "
        for element in standard:
            # print("element_counter is: ",element_counter)
            if c == temp_list[element_counter]:
                # print("Found a ", temp_list[element_counter], "at element number ", element_counter)
                # print(standard[element_counter])
                encoded_string += standard[element_counter]
                # print(encoded_string)
            element_counter += 1
    return encoded_string


temp_list = ["*"] * 26
standard = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]
revised = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

keyword = input("Please enter the key word: ").upper()
no_duplicate_letters = parse_keyword(keyword)
keyword_array  = remove_letters(revised)
shift_revised_elements_right()
insert_keyword_letters(revised)
ustring = input("Enter the string to encode: ").upper()
print(encode_the_message(ustring))