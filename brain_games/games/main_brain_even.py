import random
from brain_games.main_body import run_slider


def play():
    rule = 'Answer "yes" if number even otherwise answer "no".'
    run_slider(rule, generate_data)


def generate_data():
    number = random.randint(1, 100)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, right_answer
