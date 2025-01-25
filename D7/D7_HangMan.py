import random

stages = ['''
 +--+
 |  |
 o  |
/|\\ |
/ \\ |
    |
=========
''','''
 +--+
 |  |
 o  |
/|\\ |
/   |
    |
=========
''','''
 +--+
 |  |
 o  |
/|\\ |
    |
    |
=========
''','''
 +--+
 |  |
 o  |
/|  |
    |
    |
=========
''','''
 +--+
 |  |
 o  |
 |  |
    |
    |
=========
''','''
 +--+
 |  |
 o  |
    |
    |
    |
=========
''','''
 +--+
 |  |
    |
    |
    |
    |
=========
''']
stage_count = 0
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
display = ["_"]*len(chosen_word)
print("".join(display))

while lives > 0:
    print(stages[stage_count])
    guess = input("Guess a letter: ")
    if guess in display:
        print("You already guessed this.")
        print("".join(display))

    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        print("".join(display))
    else:
        lives -= 1
        stage_count += 1
        print(f"Wrong. {lives} lives left.")

    if "_" not in display:
        print("Win!")
        break
else:
    print("Lose. No life left.")
