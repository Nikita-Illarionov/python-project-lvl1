import prompt


def opening_speech(string):
    print('Welcome to the Brain Games!\n', string, '\n', sep='')


def body(f):
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    n = 0
    while n < 3:
        answer, right_answer = f()
        if answer == right_answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".\
Let\'s try again, {}!'.format(answer, right_answer, name))
            break
        n += 1
    if n == 3:
        print('Congratulations, {}!'.format(name))
