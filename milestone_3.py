

guess = input("Guess a Letter")

while guess.isalpha() & len(guess) == 1:
    break
else:
    print("Invalid letter. Please, enter a single alphabetical character.")

