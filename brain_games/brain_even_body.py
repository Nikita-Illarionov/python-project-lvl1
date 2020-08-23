import prompt
import random


def body():
    print('Welcome to the Brain Games!\nAnswer "yes"\
 if number even otherwise answer "no".\n')
    name = prompt.string('May I have your name? ')
    print('\n')
    n = 0
    while n < 3:
        number = random.randint(1, 1000)
        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'
        print('Question: {}'.format(number))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        elif answer == 'yes' or answer == 'no':
            print('"{}" is wrong answer ;(. Correct answer was "{}".\
Let\'s try again, {}!'.format(answer, right_answer, name))
            break
        else:
            print('Incorrect answer: you should write just "yes" or "no".\
 Let\'s try again, {}!'.format(name))
            break
        n += 1
    if n == 3:
        print('Congratulations, {}!'.format(name))
