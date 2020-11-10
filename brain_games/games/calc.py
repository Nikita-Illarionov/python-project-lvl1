import random
import operator
from brain_games.engine import run_slider


def play():
    rule = 'What is the result of the expression?'
    run_slider(rule, generate_data)


def generate_data():
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
