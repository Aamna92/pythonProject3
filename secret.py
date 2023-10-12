secret_word = "aamna92"
guess = ""

while guess != secret_word:
    guess = input("Guess the secret word: ")

    if guess != secret_word:
        print("Incorrect guess. Try again.")
    else:
        print("Congratulations! You've guessed the secret word correctly: 'aamna92'")


