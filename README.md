# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

MILESTONE 1
In milestone 1 I have connected my github to the Aicore portal in order to create a repo with hangman folder. 

MILESTONE 2
import random 

word_list = ['Mango','Banana','Apple','Kiwi','Strawberry']

guess = input("Guess a Letter")

if guess.isalpha() & len(guess) == 1:
    word = random.choice(word_list)
    print(word)
else:
    print("Oops! That is not a valid input.")
    
Above is the code i have used for completing this milestone. 
    
In this milestone i first has to connect the github repo to my local machine so that i could create and edit files. Github is a way to use git in a distributed way, you can easily share code online as well as locally. To connect to github I had to use the Git Clone command. In order to use this command, i had to get the link from hitgub, which can be found under 'code'. I copied this link and run 'git clone LINK' in the terminal, this created a remote repositary. As this is the first time i ever used github with my local machine, i was asked the the github username and a password. I entered my email and password same as the login for github, but this did not work. I continued to do some research on this and learned that i need to create and enter and API key which can be created through the settings in github. I entered this API key into the password and this linked the github account to local machine, downloading the repo. Anything done in this repo, i can modify, stage and commit the changes and use the 'git push' command to update it on github. Portal will then have access to check the code. 

One of the first tasks was to create a list containing the name of 5 fruits. I assigned this list to 'word_list'. I then went ahead and printed it to check that it was working correctly, this output the fruits on the screen. In the next task i had to import a new module called random. This random module generates random word from the given list, which in this case is 'word_list'. This is perfect hangman because we will need this to generate a random word when someone is playing it. In the next next i had to create a random.choice and pass the word_list to it and assigned this to a variable called 'word'. This line of code allows anything in the list 'word_choice' to be generated at random. i then followed this with a print(word) to make sure this works correctly. I then run this code a few times and saw the output was a random word from the list, with no pattern to it, which is correct for hangman. 

The next task was to create and valildate the input. Firstly i got the input and assinged it to a varibale called 'guess'. Then i used a if statement to check the valiation of the input and only if the input is correct, then it will run the random module to generate a randon word from the list. I used build in methods from python to check the input is an alphabect and only 1 character long. If this is true, then it will generate and print a random word, or it will print "Oops! That is not a valid input.". 
