# Program to encode/decode altered ASCII values


def encode(x,y):
    number = ord(x) + y
    print(number)

def decode(x,y):
    letter = chr(x-y)
    print(letter)


secret_key = int(input("Enter the key as an Integer "))
mode = input("Enter an 'e' to encode or a 'd' to decode ")
user_input = input("Enter a letter or number ")

if mode == 'e':
    encode(user_input, secret_key)
elif mode == 'd':
    decode(int(user_input), secret_key)
else:
    print("You failed to enter 'e' or 'd'")


