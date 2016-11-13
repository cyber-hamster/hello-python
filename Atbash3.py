"""
The Atbash cipher is a very specific case of a substitution cipher where the letters of the alphabet are reversed.
In otherwords, all As are replaced with Zs, all Bs are replaced with Ys, and so on.
Because reversing the alphabet twice will get you actual alphabet,
you can encipher and decipher a message using the exact same algorithm.
"""

standard = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", "'", "?", "!", "@", "#", "$", "%", "^",
        "&", "*", "(", ")", "-", "_", "+", "=", "[", "{", "]", "}", ";", ":",'\"', "0", "1", "2", "3", "4", "5",
        "6", "7", "9"]

reversed = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g",
          "f", "e", "d", "c", "b", "a", "Z", "Y", "X", "W", "V", "U", "T", "S", "R", "Q", "P", "O", "N", "M", "L",
        "K", "J", "I", "H", "G", "F", "E", "D", "C", "B", "A", ".", ",", "'", "?", "!", "@", "#", "$", "%", "^",
        "&", "*", "(", ")", "-", "_", "+", "=", "[", "{", "]", "}", ";", ":", '\"', "0", "1", "2", "3", "4", "5",
        "6", "7", "9"]

entry = input("Enter a string: ")
modified = ""
excluded = '"'

for c in entry:
    if c not in excluded:
        if c != " ":
            identifier = standard.index(c)
            modified = modified + (reversed[identifier])
        else:
            modified += " "

print("The new string is: ", modified)