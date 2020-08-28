import random
import operator
from brain_games.games.main_body import welcome_user, run_the_slider


def play():
    welcome_user('What is the result of the expression?')
    run_the_slider(generate_the_data)


def generate_the_data():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    if operation == '*':
        right_answer = operator.mul(a, b)
    if operation == '+':
        right_answer = operator.add(a, b)
    if operation == '-':
        right_answer = operator.sub(a, b)
    question = str(a) + ' ' + operation + ' ' + str(b)
    return question, str(right_answer)
