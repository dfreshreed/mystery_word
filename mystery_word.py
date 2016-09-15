import random
with open("/usr/share/dict/words") as lines:
    lines = lines.readlines()
comp_word = random.choice(lines)
# At the start of the game, let the user know how many letters the computer's word contains.
comp_letters = len(comp_word)
print(comp_letters)
# Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. Assume the user will only submit one letter
good_guesses = []
bad_guesses = []
letter_list = 0
print(comp_word)
print("You have 8 chances to guess my word!")


# Let the user know if their guess appears in the computer's word
# A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
# If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.
while letter_list < 8:
    guess = input("Guess a letter: ").lower()
    if guess in comp_word:
        good_guesses.append(guess)
        print("That guess is in the computer word! You have {}/8 guesses".format(letter_list))
    elif guess in good_guesses:
        print("You've already guessed that letter!")
        print(good_guesses)
    elif guess != comp_word:
        bad_guesses.append(guess)
        letter_list += 1
        print("That guess is not in the computer's word! You have {}/8 guesses".format(letter_list))
        print(bad_guesses)
    else:
        break


# Display the partially guessed word, as well as letters that have not been guessed.

# A user loses a guess only when they guess incorrectly. If they guess a letter that is in the computer's word, they do not lose a guess

# The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses, reveal the word to the user when the game ends.
