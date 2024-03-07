import random

MAX_GUESSES = 10
NO_OF_DIGITS = 3

def main():
    print('''Bagels, a deductive logic game.
          
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:

When I say:     That means:
    Pico        One digit is correct but in the wrong position.
    Fermi       One digit is correct but in the right position.
    Bagels      No digit is correct.
          
For example, if the secret number is 248 and your guess is 843, the clues would be Fermi Pico.
          '''.format(NO_OF_DIGITS))
    while True: # Main game loop
        # This stores the secret number the player needs to guess
        secretNum = generateSecretNumber()
        print('I have thought up a number.')
        print('You have {} guesses to get it.'.format(MAX_GUESSES))

        numOfGuess = 1
        while numOfGuess <= MAX_GUESSES:
            guess = ''
            # Keep looking until they enter a valid guess
            while len(guess) != NO_OF_DIGITS or not guess.isdecimal():
                print('Guess no. {}'.format(numOfGuess))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numOfGuess += 1

            if guess == secretNum:
                break # They guessed the number correctly
            if numOfGuess > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The correct number was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')

def getClues(guess, secretNum):
    '''Returns a string with pico, fermi, bagels clues based on the guess'''
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in correct place
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in a wrong place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # There are no correct digits at all
    else:
        # Sort the clues in alphabetical order so that their original order doesn't give information away
        clues.sort()
        # Return a single string by joining the string clues.
        return " ".join(clues)

def generateSecretNumber():
    '''Generates a string made up of NO_OF_DIGITS unique random digits'''
    numbers = list('0123456789') # Create a list of digits from 0 to 9
    random.shuffle(numbers) # Shuffle them into random order

    # Get the first NO_OF_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(NO_OF_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

if __name__ == "__main__":
    main()