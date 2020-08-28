import prompt


def welcome_user(string):
    print('Welcome to the Brain Games!\n', string, '\n', sep='')


def run_the_slider(generate_the_data):
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    n = 0
    while n < 3:
        question, right_answer = generate_the_data()
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print('"{}" is wrong answer ;(. Correct answer was "{}".\
Let\'s try again, {}!'.format(user_answer, right_answer, name))
            break
        n += 1
    if n == 3:
        print('Congratulations, {}!'.format(name))
