from brain_games.games.main_brain_progression import f
from brain_games.games.main_body import opening_speech, body


def main():
    opening_speech('What number is missing in the progression?')
    body(f)


if __name__ == '__main__':
    main()
