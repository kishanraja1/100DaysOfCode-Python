alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encryptFunc(textInput, shiftInput):
    wordAsList = list(textInput)
    newWord = ''
    for letter in wordAsList:
        indexNum = alphabet.index(letter)
        indexNum += int(shift)
        newWord = newWord + alphabet[indexNum]
    print(newWord)


encryptFunc(text, shift)