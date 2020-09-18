# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    guessed = True
    for i in secret_word:
        if i not in letters_guessed:
            guessed = False
    return guessed

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    partial_guess = ""
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            partial_guess += secret_word[i]
        else:
            partial_guess += "_ "
    return partial_guess

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available = string.ascii_lowercase
    available_letters = ""
    for i in available:
        if i not in letters_guessed:
            available_letters += i
    return available_letters 
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters = len(secret_word)
    guesses = 6 
    unique_words = "".join(set(secret_word))
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is", letters, "letters long.")
    letters_guessed = []
    while guesses > 0:
        score = len(unique_words)*guesses
        available = get_available_letters(letters_guessed)
        print("Available letters:", available)
        print("You have", guesses, "guesses left.")
        warnings = 3
        while True:
            guess = input("Enter your next guess: ")
            alphabet = string.ascii_letters
            if len(guess) == 1 and guess in alphabet:
                break
            if len(guess) != 1:
                warnings -= 1
                print("Your guess must have only one character! You have", warnings, "warnings left.")
            elif guess not in alphabet:
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left.")
            if warnings == 0:
                print("Too bad! You ran out of warnings! You lost one guess!")
                guesses -= 1
                warnings = 3
    
        guess = guess.lower()
        while True:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                break
            else:
                warnings -= 1
                print("You've already chosed this letter! You have", warnings, "warnings left!")
                print("You have", guesses, "guesses.")
                available = get_available_letters(letters_guessed)
                print("Available letters:", available)
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Partial word so far:", partial)
                guess = input("Enter your next guess: ")
            if warnings == 0:
                   print("Too bad! You ran out of warnings! You lost one guess!")
                   guesses -= 1
                   warnings = 3
        if guess in secret_word:
            occurences = secret_word.count(guess)
            if is_word_guessed(secret_word,letters_guessed):
                print("You nailed it. You guessed the secret word, which is:", secret_word)
                print("Your total score for this game is:", score)
                break
            else:
                print(guess, "appears in the secret word", occurences, "times! \n")
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Good guess:", partial)
        else:
            vowels = "aeiouy"
            if guess in vowels:
                guesses -= 2
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Oops! The letter", guess, "is not in my word:", partial, "\n")
            else:
                guesses -= 1
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Oops! The letter", guess, "is not in my word:", partial, "\n")
    if guesses == 0:
        print("Too bad! You've run out of guesses! The secret word was", secret_word)

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    word_without_spaces = ""
    for i in range(len(my_word)):
        if my_word[i] == " ":
            empty = my_word[i].strip()
            word_without_spaces += empty
        else:
            word_without_spaces += my_word[i]
    if len(word_without_spaces) == len(other_word):
        return True
    else:
        return False



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    my_word_without_spaces = ""
    for i in range(len(my_word)):
        if my_word[i] == " ":
            empty = my_word[i].strip()
            my_word_without_spaces += empty
        else:
            my_word_without_spaces += my_word[i]
    list_of_words = []
    final_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list_of_words.append(word)
    for j in range(len(list_of_words)):
        word_in_list = list_of_words[j]
        for i in range(len(word_in_list)):
            first_letter = True
            if word_in_list[i] != my_word_without_spaces[i] and my_word_without_spaces[i] != "_":
                first_letter = False
                break
            if first_letter:
                c = 1
                all_in = True
                while c < len(my_word_without_spaces):
                    if my_word_without_spaces[c] == "_":
                        c += 1
                    else:
                        if my_word_without_spaces[c] == word_in_list[c]:
                            all_in = True
                        else:
                            all_in = False
                            break
                        c += 1
                if all_in:
                    final_list.append(word_in_list)               
    if final_list == []:
        print("No matches found!")
    else:
        l = []
        for i in final_list:
            if i not in l:
                l.append(i)
        l.sort()
        for j in l:
            if j == l[-1]:
                print(j, end="")
            else:
                print(j, end=" ")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    letters = len(secret_word)
    guesses = 6 
    unique_words = "".join(set(secret_word))
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word that is", letters, "letters long.")
    letters_guessed = []
    guess_cont = False
    partial = ""
    while guesses > 0:
        score = len(unique_words)*guesses
        available = get_available_letters(letters_guessed)
        print("Available letters:", available)
        print("You have", guesses, "guesses left.")
        warnings = 3
        while True:
            if guess_cont:
                guess = input("Enter your next guess or enter '*' to get a hint: ")
            else:
                guess = input("Enter your next guess: ")
            alphabet = string.ascii_letters
            if len(guess) == 1 and guess in alphabet:
                guess_cont = True
                break
            if guess_cont and len(partial) > 0:
                if guess == "*":
                    print("Possible word matches are:")
                    show_possible_matches(partial)
                    print()
            if len(guess) != 1:
                warnings -= 1
                print("Your guess must have only one character! You have", warnings, "warnings left.")
            elif guess not in alphabet and guess != "*":
                warnings -= 1
                print("Oops! That is not a valid letter. You have", warnings, "warnings left.")
            if warnings == 0:
                print("Too bad! You ran out of warnings! You lost one guess!")
                guesses -= 1
                warnings = 3
    
        guess = guess.lower()
        while True:
            if guess not in letters_guessed:
                letters_guessed.append(guess)
                break
            else:
                warnings -= 1
                print("You've already chosed this letter! You have", warnings, "warnings left!")
                print("You have", guesses, "guesses.")
                available = get_available_letters(letters_guessed)
                print("Available letters:", available)
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Partial word so far:", partial)
                if guess_cont:
                    guess = input("Enter your next guess or enter '*' to get a hint: ")
                    if guess == "*":
                        print("Possible word matches are:")
                        show_possible_matches(partial)
                        print()
                else:
                    guess = input("Enter your next guess: ")
            if warnings == 0:
                   print("Too bad! You ran out of warnings! You lost one guess!")
                   guesses -= 1
                   warnings = 3
        if guess in secret_word:
            occurences = secret_word.count(guess)
            if is_word_guessed(secret_word,letters_guessed):
                print("You nailed it. You guessed the secret word, which is:", secret_word)
                print("Your total score for this game is:", score)
                break
            else:
                print(guess, "appears in the secret word", occurences, "times! \n")
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Good guess:", partial)
        else:
            vowels = "aeiouy"
            if guess in vowels:
                guesses -= 2
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Oops! The letter", guess, "is not in my word:", partial, "\n")
            elif guess not in vowels and guess != "*":
                guesses -= 1
                partial = get_guessed_word(secret_word,letters_guessed)
                print("Oops! The letter", guess, "is not in my word:", partial, "\n")
    if guesses == 0:
        print("Too bad! You've run out of guesses! The secret word was", secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)