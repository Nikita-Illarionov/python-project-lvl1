import random
from brain_games.main_body import run_slider


def play():
    rule = 'What number is missing in the progression?'
    run_slider(rule, generate_data)


def generate_data():
    step = random.randint(1, 10)
    first_number = random.randint(1, 100)
    k = random.randint(1, 10)  # number of the hidden element
    n = 11  # quality of numbers + 1
    right_answer = first_number + step * (k-1)
    question = ''
    tmp = first_number
    for i in range(1, n):
        if i == k:
            question += '.. '
        else:
            question += str(tmp) + ' '
        tmp += step
    return question, str(right_answer)
