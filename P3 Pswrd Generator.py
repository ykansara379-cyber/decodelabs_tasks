import random
print("Welcome to the password generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

Letters = int(input("How many letters do you want in your password\n"))
Symbols = int(input("How many symbols do you want in your password\n"))
Numbers = int(input("How many numbers do you want in your password\n"))

for char in range(0, Letters):
    password += random.choice(letters)

for char in range(0, Numbers):
    password += random.choice(numbers)

for char in range(0, Symbols):
    password += random.choice(symbols)


string = password
char_list = list(string)
random.shuffle(char_list)
shuffled = ''.join(char_list)
print(shuffled)