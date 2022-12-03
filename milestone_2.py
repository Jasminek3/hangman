
import random 

word_list = ['Mango','Banana','Apple','Kiwi','Strawberry']

guess = input("Guess a Letter")

if guess.isalpha() & len(guess) == 1:
    word = random.choice(word_list)
    print(word)
else:
    print("Oops! That is not a valid input.")
