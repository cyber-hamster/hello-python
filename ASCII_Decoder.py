# Take a string of numbers and convert to ASCII values

number_code = "97 134 131 131 144 145"


def add_on(x, y):
    converted = ""
    numbers = x.split()
    for number in numbers:
        temp = int(number)
        temp -= y
        converted += chr(temp)
    print(converted)


def subtract_from(s):
    converted = ""
    numbers = x.split()
    for number in numbers:
        temp = int(number)
        temp -= y
        converted += chr(temp)
    print(converted)

for counter in range(1, 35):
    add_on(number_code, counter)








# number_code = "67 104 101 101 114 115"