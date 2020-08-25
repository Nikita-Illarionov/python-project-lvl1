import random
import prompt
import math


def f():
    number = random.randint(2, 100)
    print('Question: ', number)
    answer = prompt.string('Your answer: ')
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
    return answer, right_answer
