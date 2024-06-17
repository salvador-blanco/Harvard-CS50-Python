from random import randint
def main():
    promp = "Level: "
    level = ask_level(promp)
    computer_number = randint(1,9)
    while True:
        guess = get_guess("Guess: ")
        check_win(guess, computer_number) # Exits game if win

def get_guess(promp):
    while(True):
        try:
            guess = int(input(promp))
        except ValueError:
            continue
        else:
            if guess > 0:
                return guess

def check_win(guess, computer_number):
    if guess < computer_number: #If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        print("Too small!")
    elif guess > computer_number: #If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        print("Too large!")
    else: # If the guess is the same as that integer, the program should output Just right! and exit.
        exit("Just right!")

def ask_level(promp):
    while(True):
        try:
            level = int(input(promp))
        except ValueError:
            continue
        else:
            return level

if __name__ == "__main__":
    main()
