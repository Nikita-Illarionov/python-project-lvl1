from brain_games.games.main_brain_even import f
from brain_games.games.main_body import opening_speech, body


def main():
    opening_speech('Answer "yes" if number even otherwise answer "no".')
    body(f)


if __name__ == '__main__':
    main()
