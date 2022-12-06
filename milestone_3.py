guess = input("Guess a Letter")

while True:
    guess = input('Guess a Letter')
    if guess.isalpha() & len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
