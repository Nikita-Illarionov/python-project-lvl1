from brain_games.games.main_brain_calc import f
from brain_games.games.main_body import opening_speech, body


def main():
    opening_speech('What is the result of the expression?')
    body(f)


if __name__ == '__main__':
    main()
