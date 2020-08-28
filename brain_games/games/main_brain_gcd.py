import random
from brain_games.games.main_body import welcome_user, run_the_slider


def play():
    welcome_user('Find the greatest common divisor of given numbers.')
    run_the_slider(generate_the_data)


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def generate_the_data():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    question = str(a) + ' ' + str(b)
    right_answer = find_gcd(a, b)
    return question, str(right_answer)
