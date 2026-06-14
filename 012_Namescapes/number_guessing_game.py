import random


def generate_number():
    """Generates a random number between 1 and 100

    :return: the random number between 1 and 100
    """
    number = random.randint(1, 100)
    return number


def set_difficulty(difficulty):
    """Set the difficulty to Easy, Medium, or Hard, with corresponding number of guesses set

    :param difficulty: The difficulty chosen by the user
    :return: The number of attempts allowed
    """
    if difficulty == 1:
        return 20
    elif difficulty == 2:
        return 15
    elif difficulty == 3:
        return 10
    else:
        print("Invalid choice. Defaulting to Easy.")
        return 20


def amend_difficulty(num_of_attempts):
    """Amends the number of attempts to guess the number

    :param num_of_attempts: The number of attempts remaining
    :return: The new number of attempts remaining after making a guess
    """
    if num_of_attempts > 0:
        num_of_attempts -= 1
        return num_of_attempts
    else:
        return "You Lose"


def number_guessing_game():
    """The game loop starts at the beginning of the game

    :return: None
    """
    while True:
        answer = generate_number()
        difficulty_choice = int(input("\nChoose a difficulty. Type 1 for Easy, 2 for Medium, or 3 for Hard: "))
        attempts = set_difficulty(difficulty_choice)
        print(f"You have {attempts} attempts")

        while attempts > 0:
            guess = int(input("Make a guess: "))
            if guess < answer:
                print("Too low.")
                attempts = amend_difficulty(attempts)
                print(f"You have {attempts} attempts remaining.")
            elif guess > answer:
                print("Too high.")
                attempts = amend_difficulty(attempts)
                print(f"You have {attempts} attempts remaining.")
            else:
                print(f"\nYou got it! The answer was {answer}.")
                print(f"You had {attempts} attempts remaining.")
                break
        else:
            print(f"\nYou Lose! The answer was {answer}.")

        restart = input("\nDo you want to play again? (y/n): ")

        if restart != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    print("""
╭─╴╷ ╷╭─╴╭─╮╭─╮   ╶┬╴╷ ╷╭─╴   ╭╮╷╷ ╷╭┬╮╭╮ ╭─╴╭─╮
│╶╮│ │├╴ ╰─╮╰─╮    │├─┤├╴    │╰┤│ ││││┴╮├╴ ├┬╯
╰─╯╰─╯╰─╴╰─╯╰─╯    ╵ ╵ ╵╰─╴   ╵ ╵╰─╯╵ ╵╰─╯╰─╴╵╰╴
    """)
    print(f"Welcome to the Number Guessing Game!\n{"*" * 30}")
    number_guessing_game()
