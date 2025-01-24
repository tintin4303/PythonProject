import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

display = ["_"] * len(chosen_word)
print("Welcome to Word Guessing Game!")
print(" ".join(display))

lives = 6

while lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed this letter.")
    elif guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
        print("Correct")
    else:
        lives -= 1
        print("Wrong! ", lives, " lives left.")

    print(" ".join(display))

    if "_" not in display:
        print("Win!")
        break
else:
    print("Lose. No life left.")
