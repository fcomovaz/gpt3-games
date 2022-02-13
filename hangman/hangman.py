"""
1. Get a random word from the word list.
2. Mask the word with asterisks: e.g. ******
3. Print the masked word.
4. Loop until the user guesses the word or runs out of guesses.
    a. Get a guess from the user.
    b. If the guess is in the guessed letters, print a message and continue.
    c. If the guess is not in the word, decrement the number of guesses and print a message.
    d. If the guess is in the word, fill in the corresponding asterisks.
    e. Print the masked word.
    f. Check if the user won.
"""
import random

def get_secret_word(word_file="words.txt"):
    with open(word_file) as f:
        good_words = []
        for i in f:
            i = i.strip()
            if len(i) <= 6:     # No short words
                continue
            if not i.isalpha(): # No punctuation
                continue
            if i[0].isupper():  # No proper nouns
                continue
            good_words.append(i)
    return random.choice(good_words)

def mask_secret_word(secret_word, guessed_letters):
    masked_word = ""
    for i in secret_word:
        if i in guessed_letters:
            masked_word += i
        else:
            masked_word += "*"
    return masked_word

def check_win(secret_word, guessed_letters):
    for i in secret_word:
        if i not in guessed_letters:
            return False
    return True

def main():
    secret_word = get_secret_word()
    guessed_letters = []
    masked_word = mask_secret_word(secret_word, guessed_letters)
    print("Welcome to Hangman!")
    print(masked_word)
    while True:
        guess = input("Guess a letter: ")
        if guess in guessed_letters:
            print("You already guessed that!")
            continue
        guessed_letters.append(guess)
        masked_word = mask_secret_word(secret_word, guessed_letters)
        print(masked_word)
        if check_win(secret_word, guessed_letters):
            print("You win!")
            break

if __name__ == "__main__":
    main()