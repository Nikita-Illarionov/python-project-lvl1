import random
from brain_games.games.main_body import welcome_user, run_the_slider


def play():
    welcome_user('What number is missing in the progression?')
    run_the_slider(generate_the_data)


def generate_the_data():
    step = random.randint(1, 10)
    tmp = random.randint(1, 100)  # first number
    k = random.randint(1, 10)  # number of the hidden element
    n = 11  # quality of numbers + 1
    right_answer = tmp + step * (k-1)
    question = ''
    for i in range(1, n):
        if i == k:
            question += '.. '
        else:
            question += str(tmp) + ' '
        tmp += step
    return question, str(right_answer)
