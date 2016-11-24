# ROT13 ("rotate by 13 places", sometimes hyphenated ROT-13) is a simple letter substitution cipher that replaces
# a letter with the letter 13 letters after it in the alphabet. ROT13 is a special case of the Caesar cipher,
# developed in ancient Rome.

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O","P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

letter = input("Enter a letter: ").upper()
location = 0

# Determine the position in the list for the entered letter
for i in range(0,25):
    if alphabet[i] == letter:
        location = i
print("The letter is at position ", location)

# Calculate the position on the list for the letter shift
new_location = location + 13
print("Number of places to be shifted is: ", new_location)

# Loop around to the beginning of the list when the new_location calculates to greater than 25. List index is 0-25.
if new_location > 25:
    new_location = new_location - 26
    print("Loop around location is ", new_location)

print("The ROT-13 letter is ", alphabet[new_location])