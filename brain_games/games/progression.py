import random
from brain_games.engine import run_slider


def play():
    rule = 'What number is missing in the progression?'
    run_slider(rule, generate_data)


def generate_data():
    progression_length = 10
    step = random.randint(1, 10)
    first_number = random.randint(1, 100)
    hidden_element_index = random.randint(0, progression_length - 1)
    right_answer = first_number + step * hidden_element_index
    question = ''
    for k in range(progression_length):
        if k == hidden_element_index:
            question += '.. '
        else:
            question += str(first_number + step * k) + ' '
    question = question[:-1]  # deleting the excess space
    return question, str(right_answer)
