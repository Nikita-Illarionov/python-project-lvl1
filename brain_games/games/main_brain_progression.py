import random
import prompt


def f():
    step = random.randint(1, 10)
    tmp = random.randint(1, 100)  # first number
    k = random.randint(1, 10)  # number of the hidden element
    right_answer = tmp + step * (k-1)
    print('Question: ', end='')
    for i in range(1, 11):
        if i == k:
            print('..', end=' ')
        else:
            print(tmp, end=' ')
        tmp += step
    answer = prompt.string('\nYour answer: ')
    return answer, str(right_answer)
