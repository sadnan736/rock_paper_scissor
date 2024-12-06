import random

def pick_choice(user_input):
    if user_input == 'r':
        return 'rock'
    if user_input == 'p':
        return 'paper'
    if user_input == 's' or user_input == 'scissors':
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

def ending_print(uc,bc):
    print("""
██████████████████████████████████████████████████████████████████
█▄─▄▄─█▄─▀█▄─▄█▄─▄▄▀███─▄▄─█▄─▄▄─███▄─▀█▀─▄██▀▄─██─▄─▄─█─▄▄▄─█─█─█
██─▄█▀██─█▄▀─███─██─███─██─██─▄██████─█▄█─███─▀─████─███─███▀█─▄─█
▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▄▀▄▄▄▀▀▀▀▀▄▄▄▀▄▄▄▀▄▄▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▀▄▀""")

    if uc>bc:
        return """
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝"""

    elif bc>uc:
        return """
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░██████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔════╝██╔════╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║╚█████╗░█████╗░░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║░╚═══██╗██╔══╝░░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝██████╔╝███████╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░╚═════╝░╚══════╝"""

    else:
        return '''
██╗████████╗██╗░██████╗  ░█████╗░  ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
██║╚══██╔══╝╚█║██╔════╝  ██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
██║░░░██║░░░░╚╝╚█████╗░  ███████║  ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
██║░░░██║░░░░░░░╚═══██╗  ██╔══██║  ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
██║░░░██║░░░░░░██████╔╝  ██║░░██║  ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
╚═╝░░░╚═╝░░░░░░╚═════╝░  ╚═╝░░╚═╝  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░'''

def rounds_calc():
    round_inp = input("How many rounds? [Odds Recommended, default 3]")

    if round_inp == '':
        return 3

    try:
        return int(round_inp)
    except ValueError:
        print("Please enter a valid positive, integer (no fractional) value or keep blank")
        return rounds_calc()

    return 3

def rock_paper_scissors():
    user_choice = input("'Rock', 'Paper', 'Scissor' - INPUT! (r/p/s)\n").lower()
    game_outcomes = ['rock', 'paper', 'scissor']
    bot_choice = random.choice(game_outcomes)


    if user_choice not in game_outcomes:
        user_choice = pick_choice(user_choice)
        if user_choice is None:
            print("You got confused, Try Again!")
            rock_paper_scissors()

    print('You chose:')
    print_symbols(user_choice)
    print('Opponent Chose:')
    print_symbols(bot_choice)

    if user_choice == bot_choice:
        return None

    elif user_choice == 'rock':
        if bot_choice != 'paper':
            return True
        else:
            return False

    elif user_choice == 'paper':
        if bot_choice != 'scissor':
            return True
        else:
            return False

    elif user_choice == 'scissor':
        if bot_choice != 'rock':
            return True
        else:
            return False

rounds = rounds_calc()
user_score = 0
bot_score = 0
print(f'Your Score: {user_score}\nAI Score:{bot_score}')
for i in range(rounds):
    print(f'Round {i+1}, Begin!')
    status = rock_paper_scissors()

    if status is None:
        print("It's a Draw!")
    elif status:
        user_score += 1
        print('You Win!')
    elif not status:
        bot_score += 1
        print('You Loose.')

    print(f'Your Score: {user_score}\nAI Score:{bot_score}')

print(ending_print(user_score, bot_score))