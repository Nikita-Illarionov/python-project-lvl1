import prompt
import random


def f():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])
    if operator == '*':
        right_answer = a * b
    if operator == '+':
        right_answer = a + b
    if operator == '-':
        right_answer = a - b
    print('Question: {} {} {}'.format(str(a), operator, str(b)))
    answer = prompt.string('Your answer: ')
    return answer, str(right_answer)
