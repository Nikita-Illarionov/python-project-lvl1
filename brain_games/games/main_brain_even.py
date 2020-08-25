import random
import prompt


def f():
    number = random.randint(1, 100)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    print('Question: {}'.format(number))
    answer = prompt.string('Your answer: ')
    return answer, right_answer
