import random

letters_guessed = list()
incorrect_guesses = list()

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for i in letters_guessed:
        if(secret_word.find(i) == -1):
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    word_in_progress = list()
    for i in secret_word:
        if(letters_guessed.find(i, 0, len(secret_word)) != -1):
            word_in_progress.append(i)
        else:
            word_in_progress.append("_")
    result = "".join(word_in_progress)
    return result


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    temp = "".join(incorrect_guesses)
    if((temp.find(guess) != -1)):
        print("You've already guessed this letter")
    else:
        incorrect_guesses.append(guess)
    if(secret_word.find(guess) != -1):
        incorrect_guesses.pop(len(incorrect_guesses)-1)
        return True
    return False

def get_guess():
    guess = input("Please enter 1 letter: ")
    if(len(guess) != 1):
        print("Please enter only 1 letter.")
        guess = ""
        get_guess()
    letters_guessed.append(guess)
    return guess

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    guess = get_guess()

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    is_guess_in_word(guess, secret_word)
    #TODO: show the guessed word so far
    letters_guessed_to_pass = "".join(letters_guessed)
    result = get_guessed_word(secret_word, letters_guessed_to_pass)#"abcdefghijklmnopqurstuvwxyz")
    print(result)
    print("you have " + str(len(secret_word) - len(incorrect_guesses)) + " incorrect guesses left")
    #TODO: check if the game has been won or lost
    if(result.find("_") == -1):
        print("GAME WON")
        print("Word was: " + secret_word)
        print("\n--------------------------------")
    elif(len(incorrect_guesses) < len(secret_word)):
        print("\n-------------------------------")
        spaceman(secret_word)
    else:
        print("Sorry you didnt win...")
        print("Word was: " + secret_word)
        print("\n--------------------------------")

#These function calls that will start the game
keep_playing = True
while(keep_playing == True):
    secret_word = load_word()
    print("Welcome to Spaceman!")
    print("The secret word contains: " + str(len(secret_word)) +" letters")
    print("you have " + str(len(secret_word)) + " incorrect guesses, please enter one word per round")
    print("--------------------------------")
    spaceman(secret_word)

    keep_playing = False

    temp = input("Enter 'yes' if you would like to keep playing\n")
    if(temp == 'yes'):
        keep_playing = True
