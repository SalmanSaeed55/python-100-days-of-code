import random
from words import words

HANGMAN_ASCII_ART = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O  |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O  |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


def chosen_word():
    word = random.choice(words)
    return word


def hidden_word(word, letters):
    word_length = len(word)
    if letters:
        display = ""
        for char in word:
            if char in letters:
                display += char + " "
            else:
                display += "_ "
        print(f"The word is: {display}")
    else:
        print(f"The word is: {"_ " * word_length}")


def letter_check(word, letter):
    for char in word:
        if letter == char:
            return True
    return False


guesses = -1
guessed_letters = []
guessing_word = chosen_word()

while True:
    hidden_word(guessing_word, guessed_letters)
    word_set = set(guessing_word)

    letter_guess = input("Guess a letter: ").lower()
    check_word = letter_check(guessing_word, letter_guess)

    if check_word:
        if letter_guess not in guessed_letters:
            print("Correct!")
            guessed_letters.append(letter_guess)

            if len(word_set) == len(guessed_letters):
                print(f"You win! The word was {guessing_word}")
                break
    else:
        print("Wrong!")
        guesses += 1
        if guesses < len(HANGMAN_ASCII_ART) - 1:
            print(HANGMAN_ASCII_ART[guesses])
        elif guesses == len(HANGMAN_ASCII_ART) - 1:
            print(HANGMAN_ASCII_ART[guesses])
            print(f"You Lose!\nThe word was {guessing_word}")
            break