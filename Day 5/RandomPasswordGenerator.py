import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# My solution.
if nr_letters > 0:
    mix = random.choices(letters, k=nr_letters)
    if nr_symbols > 0:
        mix2 = random.choices(symbols, k=nr_symbols)
        if nr_numbers > 0:
            mix3 = random.choices(numbers, k=nr_numbers)

            mix.extend(mix2)
            mix.extend(mix3)
            random.shuffle(mix)
            mix = "".join(mix)
            print("Your password is: " + mix)

# The code below is based on the Instructor's solution
# password = ""
# for char in range(0, nr_letters):
#     password += random.choice(letters)
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# password = list(password)
# random.shuffle(password)
# password = "".join(password)
# print("Your password is: " + password)