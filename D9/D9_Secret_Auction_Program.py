logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
dict = {}
print(logo)
loop = True
while loop:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict[name] = bid
    q = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if q == "no":
        person = ""
        maxNum = 0
        for i in dict:
            if dict[i] > maxNum:
                maxNum = dict[i]
                person = i
        print(f"The winner is {person} with a bid of ${dict[person]}.")
        break
    else:
        print("\n"*100)