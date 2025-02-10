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
bids = {}
print("Welcome to the Secret Auction Program.")
print(logo)
loop = True
while loop:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    q = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if q == "no":
        person = ""
        maxNum = 0
        for i in bids:
            if bids[i] > maxNum:
                maxNum = bids[i]
                person = i
        print(f"The winner is {person} with a bid of ${bids[person]}.")
        break
    else:
        print("\n"*100)