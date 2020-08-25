import random
import prompt


def f():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    print('Question: {} {}'.format(a, b))
    answer = prompt.string('Your answer: ')
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    right_answer = a + b
    return answer, str(right_answer)
