import random

def pick_choice(user_input):
    if user_input == 'r':
        return 'rock'
    if user_input == 'p':
        return 'paper'
    if user_input == 's':
        return 'scissor'
    if user_input == 'scissors':
        return 'scissor'

    return None

def print_symbols(symbol):

    if symbol == 'rock':
        print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')

    elif symbol == 'scissor':
        print( '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
    
    else:
        print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')

game_outcomes = ['rock', 'paper', 'scissor']
user_choice = input("'Rock', 'Paper', 'Scissor' - INPUT! (r/p/s)\n").lower()
bot_choice = random.choice(game_outcomes)


if user_choice not in game_outcomes:
    user_choice = pick_choice(user_choice)
    if user_choice is None:
        print("You got confused, you loose.")

print('You chose:')
print_symbols(user_choice)
print('Opponent Chose:')
print_symbols(bot_choice)

if user_choice == bot_choice:
    print("It's a Draw!")

elif user_choice == 'rock':
    if bot_choice != 'paper':
        print('You Win!')
    else:
        print('You Loose.')
        
elif user_choice == 'paper':
    if bot_choice != 'scissor':
        print('You Win!')
    else:
        print('You Loose.')
        
elif user_choice == 'scissor':
    if bot_choice != 'rock':
        print('You Win!')
    else:
        print('You Loose.')