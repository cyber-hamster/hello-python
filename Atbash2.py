"""
The Atbash cipher is a very specific case of a substitution cipher where the letters of the alphabet are reversed.
In otherwords, all As are replaced with Zs, all Bs are replaced with Ys, and so on.
Because reversing the alphabet twice will get you actual alphabet,
you can encipher and decipher a message using the exact same algorithm.
"""

standard = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
          "u", "v", "w", "x", "y", "z"]

reversed = ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g",
          "f", "e", "d", "c", "b", "a"]

mode = input("Enter 'e' to encode or 'd' to decode: ")
entry = input("Enter a string: ").lower()
modified = ""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

if mode == 'e':
    for c in entry:
        if c not in punctuations:
            if c !=" ":
                identifier = standard.index(c)
                modified = modified + (reversed[identifier])
            else:
                modified += " "

elif mode == 'd':
    for c in entry:
        if c not in punctuations:
            if c !=" ":
                identifier = reversed.index(c)
                modified = modified + (standard[identifier])
            else:
                modified += " "

else:
    print("Bad User entry!")

print("The new string is: ", modified)