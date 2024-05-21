import random

def main():
    random_number = random.randint(1,99)
    run = True
    while run:
        guess_number = int(input("Guess the number between 1 to 99: "))
        if guess_number > random_number:
            print(f"Oops! Too high!")
        elif guess_number < random_number:
            print(f"Oops! Too low!")
        else:
            print(f"Yay! You guess correctly")
            play_again = input("Play again (Y/N)?: ")
            if play_again == "N":
                run = False
            else:
                random_number = random.randint(1,99)


if __name__ == "__main__":
    main()