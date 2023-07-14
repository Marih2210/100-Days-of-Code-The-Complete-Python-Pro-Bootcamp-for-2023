#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = [] 
for letter in range(0, nr_letters):
    total_letters = len(letters)
    letter = random.randint(0, total_letters - 1)
    letras = letters[letter]
    password_letters.append(letras)

password_symbols = [] 
for symbol in range(0, nr_symbols):
    total_symbols = len(symbols)
    symbol = random.randint(0, total_symbols - 1)
    simbolos = symbols[symbol]
    password_symbols.append(simbolos)

password_numbers = [] 
for letter in range(0, nr_numbers):
    total_numbers = len(numbers)
    number = random.randint(0, total_numbers - 1)
    numeros = numbers[number]
    password_numbers.append(numeros)
    
senha_completa  = password_letters + password_symbols + password_numbers

random.shuffle(senha_completa)
senha_completa_str = ''.join(senha_completa)

print(f"Here is your password: {senha_completa_str}")
