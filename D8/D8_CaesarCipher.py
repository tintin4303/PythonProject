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


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
loop = True
while loop == True:
    messageQ = input("Type your message:\n")
    shiftQ = input("Type the shift number:\n")
    directionQ = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    print("Here's the result: ", cipher(messageQ, shiftQ,directionQ))
    q = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if q == "no":
        print("Bye.")
        break