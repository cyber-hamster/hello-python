# Experiments using the Book Cipher algorithm
"""
A book cipher uses a large piece of text to encode a secret message. Without the key (the piece of text)
it is very difficult to decrypt the secret message.

To implement a book cipher, each word in the secret message would be replaced with a number
which represents the same word in the book. For example, if the word "attack"
appeared in the book as word number 713, then "attack" would be replaced with this number. T
he result would be an encoded message that looked something like this.

713 23 245 45 124 1269 586 443 8 234
To decipher the message you simply count the number of words in the book and write down each one.
"""

sentence = input("Enter a sentence, ").lower()
word_to_find = input("Enter a word from the sentence, ").lower()
words = sentence.split()
# Splits the string 'sentence' and returns a list of words in it. Split() method splits on default delimiters.
for pos in range(len(words)):
    if word_to_find == words[pos]:
        print(pos+1)
# words[pos] corresponds to the word present in the 'words' list at 'pos' index position.
