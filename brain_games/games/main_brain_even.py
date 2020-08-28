import random
from brain_games.games.main_body import welcome_user, run_the_slider


def play():
    welcome_user('Answer "yes" if number even otherwise answer "no".')
    run_the_slider(generate_the_data)


def generate_the_data():
    number = random.randint(1, 100)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = str(number)
    return question, right_answer
