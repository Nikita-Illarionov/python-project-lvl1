import random
import math
from brain_games.main_body import run_slider


def play():
    rule = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    run_slider(rule, generate_data)


def is_prime(number):
    if number < 2:
        return False
    i = 2
    limit = int(math.sqrt(number))
    remainder = True
    while i <= limit:
        remainder = number % i != 0
        if not remainder:
            return False
        i += 1
    return True


def generate_data():
    number = random.randint(2, 100)
    question = str(number)
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
