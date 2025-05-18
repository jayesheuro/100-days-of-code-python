import random

letters = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
numbers = [str(i) for i in range(10)]
symbols = random.sample(['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?', '|', '\\'], 10)
accumulated_characters = [letters] + [numbers] + [symbols]

print("Welcome to the Password Generator!")

num_letters = int(input("How many letters would you like in your password?"))
num_numbers = int(input("How many numbers would you like in your password?"))
num_symbols = int(input("How many symbols would you like in your password?"))


password = ""
pass_length = num_letters + num_numbers + num_symbols

l = 0
n = 0
s = 0
choices = [1,2,3]

for i in range(0, pass_length):
    if(l == num_letters and choices.__contains__(1)):
        choices.remove(1)
    if(n == num_numbers and choices.__contains__(2)):
        choices.remove(2)
    if(s == num_symbols and choices.__contains__(3)):
        choices.remove(3)

    choice = random.choice(choices)
    if(choice == 1 and l < num_letters):
        password += random.choice(letters)
        l+=1
    if(choice == 2 and n < num_numbers):
        password += random.choice(numbers)
        n+=1
    if(choice == 3 and s < num_symbols):
        password += random.choice(symbols)
        s+=1

# easy 

# for i in range(0, num_letters):
#     password += random.choice(letters)

# for i in range(0, num_symbols):
#     password += random.choice(symbols)

# for i in range(0, num_numbers):
#     password += random.choice(numbers)


print(password)
