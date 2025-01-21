import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_pw = ""
for char in range(nr_letters):
    easy_pw += random.choice(letters)
for symbol in range(nr_symbols):
    easy_pw += random.choice(symbols)
for number in range(nr_numbers):
    easy_pw += random.choice(numbers)
print("Easy Password: ", easy_pw)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
hard_pw = ""
for char in range(nr_letters):
    password_list.append(random.choice(letters))
for symbol in range(nr_symbols):
    password_list.append(random.choice(symbols))
for number in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
for each in password_list:
    hard_pw += each
print("Hard Password: ",hard_pw)

# for i in range(len(password_list)):
#     rand_word = random.choice(password_list)
#     hard_pw += rand_word
#     password_list.remove(rand_word)
