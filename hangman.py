#This code I built with the assistance of a tutorial, I was learning by interpreting the steps.

#Import random module to randomize the choice of word to be guessed
import random

#Make a list of words that can be chosen in the game
word_list = [
    'travel',
    'airplane',
    'ship',
    'luggage',
    'location',
    'gps',
    'beach',
    'mountain',
    'metropolis'
]

#Code the random choice of word from the the word_list
def get_word():
    word = random.choice(word_list)
    return word.upper()

#Code the introduction to the game and basic parameters
def play(word):
    #Define the variable word_completion, that use "_" multiplied by the length of the word, so each letter goes in a _
    word_completion = "_" * len(word)
    #Code that the word is not yet guessed
    guessed =  False
    #Code that no letter has been guessed
    guessed_letters = []
    #Code that no words have been guessed
    guessed_words = []
    #Code the number of available tries
    tries = 6
    
    #Code the introduction
    print ("Lets play hangman! ")
    print (display_hangman(tries))
    
    #Code to load the "word_completion" defined above
    print (word_completion)
    print ("\n")
    
    #Code not to ask for me guesses once the number of tries reached 0
    while not guessed and tries > 0:
    
    #Code to print the message to guess
        guess = input("Please guess a letter or word ").upper()
        
    #Code to ensure only 1 letter at a time is guessed and that it is alphabetical
        if len(guess) == 1 and guess.isalpha():
        
    #Code to avoid losing point for guessing the same letter twice 
            if guess in guessed_letters:
                print ("You already tried that letter ", guess)
            elif guess not in word:
                print (guess, "is not in the word ")
    
    #Code to reduce the number of available tries in the match
                tries -= 1
                
    #Code to append the guessed letter to the guessed list
                guessed_letters.append(guess)
                
    #If the guess is valid, meaning it does not fall in the previous situations, guess is correct
            else:
                print ('Good job! guess is a correct letter! ')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print ('You already guessed that word ', guess)
            elif guess !=word:
                print ('Wrong one! ')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else: 
            print ("Not a valid guess ")

        print (display_hangman(tries))
        print (word_completion)
        print ("\n")
        
#Code of message to winner
    if guessed:
        print ("Congratulations! You got it right! You win! ")
        
#Code of message to not winner
    else:
        print ("You ran out of tries and got hanged! The word was " + word  + ". Maybe next time! ")

#Define the visual of our hangman through the different stages
def display_hangman(tries):
    stages = [  """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                """,
                """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                ""","""
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
                    -
                ""","""
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      
                    |     
                    -
                ""","""
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      
                    |     
                    -
                ""","""
                    --------
                    |      |
                    |      O
                    |      |
                    |      
                    |     
                    -
                ""","""
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                ""","""
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                """]  
    return stages[tries]

#Code of replay
def main():
    word = get_word()
    play(word)
    while input("Play again? Y/N ").upper() == "Y":
        word = get_word()
        play(word)

#Do not understand this part of the code, but it does not run without it
if __name__ == "__main__":
    main()
