#Password Generator Project
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

# letters_lenght = len(letters)
# numbers_lenght = len(numbers)
# symbols_lenght = len(symbols)

# password = ' '
# for i in range(nr_letters):
#   random_letter_index = random.randint(0, letters_lenght-1)
#   random_letter = letters[random_letter_index]
#   password = password + random_letter

# for i in range(nr_symbols):
#   random_symbol_index = random.randint(0, symbols_lenght-1)
#   random_symbol = symbols[random_symbol_index]
#   password = password + random_symbol

# for i in range(nr_numbers):
#   random_number_index = random.randint(0, numbers_lenght-1)
#   random_number = numbers[random_number_index]
#   password = password + random_number
# print(password)


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_lenght = len(letters)
numbers_lenght = len(numbers)
symbols_lenght = len(symbols)

password = []
for i in range(nr_letters):
  random_letter_index = random.randint(0, letters_lenght-1)
  random_letter = letters[random_letter_index]
  password.append(letters[i])

for i in range(nr_symbols):
  random_symbol_index = random.randint(0, symbols_lenght-1)
  random_symbol = symbols[random_symbol_index]
  password.append(symbols[i])

for i in range(nr_numbers):
  random_number_index = random.randint(0, numbers_lenght-1)
  random_number = numbers[random_number_index]
  password.append(numbers[i])

print(password)
random.shuffle(password)
password = ''.join(password)
print(f"Your password is {password}.")
