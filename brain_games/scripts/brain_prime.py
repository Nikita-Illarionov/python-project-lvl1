from brain_games.games.main_brain_prime import f
from brain_games.games.main_body import opening_speech, body


def main():
    opening_speech('Answer "yes" if given number is prime.\
 Otherwise answer "no".')
    body(f)


if __name__ == '__main__':
    main()
