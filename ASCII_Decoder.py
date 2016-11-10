# Take a string of numbers and convert to ASCII values


def decode(x, y, z):
    converted = ""
    numbers = x.split()
    for number in numbers:
        decoding = int(number)
        if z == "a":
            decoding += y
        elif z == "s":
            decoding -= y
        converted += chr(decoding)
    print(converted)

# These numbers each have had 30 added to the ASCII character number. Originals 67 104 101 101 114 115"
number_code = input("Enter numbers to decode like this 97 134 131 131 144 145: ")
mode = input("Enter an 'a' to add or an 's' to subtract: ")

if (mode == "a") or (mode == "s"):
    for counter in range(1, 51):
        decode(number_code, counter, mode)
else:
    print("Entry Error")










