import random
import sys
from string import ascii_lowercase
with open("/usr/share/dict/words") as lines:
    lines = lines.readlines()


# print(comp_word)


def word_game():
    comp_word = random.choice(lines).lower().replace("\n", "")
    comp_letters = len(comp_word)
    good_guesses = []
    bad_guesses = []
    letter_list = 0

    print("Welcome to Mystery Word! You have 8 chances to guess my word! My word has {} letters in it".format(len(comp_word)))
    # print(comp_word)
    blank_word = list("_" * comp_letters)
    unused_words = list(ascii_lowercase)
    while letter_list < 8:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("That's more than one letter! Guess again")
            continue
        if guess in comp_word:
            if guess in good_guesses:
                print("You've already guessed that letter! Please try again!")
            good_guesses.append(guess)
            for current_location, current_letter in enumerate(comp_word):
                if guess == current_letter:
                    blank_word[current_location] = guess
            print("That guess is in the computer word! You have {}/8 guesses".format(letter_list))
            print(*blank_word)
            if guess in unused_words:
                unused_words.remove(guess)
            print(*unused_words)

            if blank_word == list(comp_word):
                print ("You win!")
                sys.exit()
        elif guess in bad_guesses:
            print("you already guessed that letter")

        else:
            bad_guesses.append(guess)
            letter_list += 1
            print("That guess is not in the computer's word! You have {}/8 guesses".format(letter_list))

    if letter_list == 8:
        print("Game Over! Thanks for playing! You had {} wrong guesses. My word was {}.".format(letter_list, comp_word))


def replay():
    play_again = input("Do you want to play again? Y/n ").lower()
    if play_again != 'n':
        # print(play_again)
        return word_game()
    else:
        print("Bye")
        sys.exit()

word_game()
replay()
