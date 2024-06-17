import random


def main():
    score = 0
    times_ask = 3
    level = get_level("Level: ")

    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        user_answer = check_question(x,y,answer,times_ask)

        score += user_answer

    print("Score: {}".format(score))

def check_question(x,y,answer,times_ask):

    for _ in range(times_ask):
        user_answer = input("{} + {} = ".format(x,y))
        try:
            if answer == int(user_answer):
                return 1
            else:
                print("EEE")
        except ValueError:
            print("EEE")
    print("{} + {} = {}".format(x,y, answer))
    return 0

def get_level(promp = "Level: "):
    while(True):
        try:
            level = int(input(promp))
        except ValueError:
            continue
        else:
            if 1 <= level <=3:
                return level
            else:
                continue


def generate_integer(level):

    if not (1 <= level <= 3):
        raise ValueError

    min_num = int(10 ** (level - 2)) * 10
    max_num = int(10 ** level) - 1

    integer = random.randint( min_num, max_num )

    return integer

if __name__ == "__main__":
    main()
