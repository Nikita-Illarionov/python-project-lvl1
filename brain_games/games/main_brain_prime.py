import random
import math
from brain_games.main_body import run_slider


def play():
    rule = 'Answer "yes" if given number is prime.\
 Otherwise answer "no".'
    run_slider(rule, generate_data)


def isPrime(number):
    result = True
    i = 2
    limit = int(math.sqrt(number))
    while result and i <= limit:
        result = number % i != 0
        i += 1
    return 'yes' if result else 'no'


def generate_data():
    number = random.randint(2, 100)
    question = str(number)
    right_answer = isPrime(number)
    return question, right_answer
