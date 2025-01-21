import random

List = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''',
        '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
        ''',
        '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
        '''
        ]

print("Welcome to Rock, Paper, Scissor.")
player = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))
while 0 <= player <= 2:
    print(List[player])
    opponent = random.randint(0,2)
    print("Opponent\n", List[opponent])

    if player == 0:
        if opponent == 1:
            print("You lose.")
        elif opponent == 2:
            print("You win!")
        else:
            print("Tie!")
    elif player == 1:
        if opponent == 2:
            print("You lose.")
        elif opponent == 0:
            print("You win!")
        else:
            print("Tie!")
    elif player == 2:
        if opponent == 0:
            print("You lose.")
        elif opponent == 1:
            print("You win!")
        else:
            print("Tie!")
    play_again = input("Would you like to play again? (Yes/No): ").lower()
    if play_again == "yes":
        player = int(input("What do you choose? 0 for Rock, 1 for Paper or 2 for Scissors: "))
    else:
        print("Bye!")
        break



else:
    print("Invalid choice. Choose again.")