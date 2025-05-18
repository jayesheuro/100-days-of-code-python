import random

choice = int(input('''
WELCOME TO ROCK PAPER SCISSORS
Enter your choice - 
1 for ROCK 🪨
2 for PAPER 📃
3 for SCISSORS ✂️
'''))


choices = ['rock', 'paper', 'scissors']

computer_choice = choices[random.randint(0, 2)]

if choice == 1 or choice == 2 or choice == 3:
    users_choice = choices[choice-1]
    if computer_choice == users_choice:
        print(f'CPU chose {computer_choice}')
        print("DRAW")
    else:
        if computer_choice == choices[0]:
            print(f'CPU chose {choices[0]}')
            if users_choice == choices[1]:
                print("USER WINS")
            else:
                print("CPU WINS")
        elif computer_choice == choices[1]:
            print(f'CPU chose {choices[1]}')
            if users_choice == choices[0]:
                print("CPU WINS")
            else:
                print("USER WINS")
        else:
            print(f'CPU chose {choices[2]}')
            if users_choice == choices[0]:
                print("USER WINS")
            else:
                print("CPU WINS")
else:
    print("INVALID USER CHOICE")