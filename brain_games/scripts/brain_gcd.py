from brain_games.games.main_brain_gcd import f
from brain_games.games.main_body import opening_speech, body


def main():
    opening_speech('Find the greatest common divisor of given numbers.')
    body(f)


if __name__ == '__main__':
    main()
