#%%
import random 

word_list = ['Mango','Banana','Apple','Kiwi','Strawberry']

while True:
    guess = input('Guess a Letter')
    if guess.isalpha() & len(guess) == 1:
        word = random.choice(word_list)
        print(word)
        if guess in word:
            print(f'Good guess! "{guess}" is in the word.')
        else:
            print(f'Sorry, {guess} is not in the word. Try again.')
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        break

# %%
