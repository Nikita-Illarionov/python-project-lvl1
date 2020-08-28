import random
import math
from brain_games.games.main_body import welcome_user, run_the_slider


def play():
    welcome_user('Answer "yes" if given number is prime.\
 Otherwise answer "no".')
    run_the_slider(generate_the_data)


def generate_the_data():
    number = random.randint(2, 100)
    question = str(number)
    result = True
    i = 2
    limit = int(math.sqrt(number))
    while result and i <= limit:
        result = number % i != 0
        i += 1
    if result:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
