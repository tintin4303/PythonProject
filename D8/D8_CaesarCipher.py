def cipher(message, shift, direction):
    shift = int(shift)
    if direction == "decode":
        shift = -shift
    new_message = ""
    for letter in message:
        if letter.isalpha():
            base = ord('A') if letter.isupper() else ord('a')
            shifted = (ord(letter) - base + shift) % 26 + base
            shifted_letter = chr(shifted)
            new_message+=shifted_letter
        else:
            new_message += letter
    return new_message

messageQ = input("Type your message:\n")
shiftQ = input("Type the shift number:\n")
directionQ = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()

print("Here's the result: ", cipher(messageQ, shiftQ,directionQ))
