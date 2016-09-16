import random
import sys
from string import ascii_lowercase
with open("/usr/share/dict/words") as lines:
    lines = lines.readlines()


def level_choice():
    comp_word = random.choice(lines).lower().replace("\n", "")
    print("Which mode would you like to play?")
    mode_choice = input("[E]asy, [N]ormal, [H]ard: ").lower()
    if mode_choice == 'e':
        while True:
                random_word = comp_word
                if len(random_word) <= 6:
                    word_game(random_word)
                else:
                    comp_word = random.choice(lines).lower().replace("\n", "")

    if mode_choice == 'n':
        while True:
            random_word = comp_word
            if len(random_word) <= 6 and len(random_word) < 10:
                word_game(random_word)
            else:
                comp_word = random.choice(lines).lower().replace("\n", "")
    if mode_choice == 'h':
        while True:
            random_word = comp_word
            if len(random_word) >= 10:
                word_game(random_word)
            else:
                comp_word = random.choice(lines).lower().replace("\n", "")

    return(random_word)

# print(comp_word)


def word_game(random_word):
    # comp_word = random.choice(lines).lower().replace("\n", "")
    comp_word = random_word
    comp_letters = len(comp_word)
    good_guesses = []
    bad_guesses = []
    letter_list = 0
    # print(comp_word)
    # easy_mode = []
    # normal_mode = []
    # hard_mode = []
    print("You have 8 chances to guess my word! My word has {} letters in it".format(len(comp_word)))
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
                replay()
        elif guess in bad_guesses:
            print("you already guessed that letter")

        else:
            bad_guesses.append(guess)
            letter_list += 1
            print("That guess is not in the computer's word! You have {}/8 guesses".format(letter_list))

    if letter_list == 8:
        print('\n')
        print("GAME OVER! Thanks for playing! You had {} wrong guesses. My word was {}.".format(letter_list, comp_word))
        replay()


def replay():
    play_again = input("Do you want to play again? Y/n ").lower()
    if play_again != 'n':
        # print(play_again)
        level_choice()
    else:
        print("\nBye")
        sys.exit()
#
level_choice()
# word_game()
# replay()
