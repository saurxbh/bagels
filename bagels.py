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

def generateSecretNumber():
    '''Generates a string made up of NO_OF_DIGITS unique random digits'''
    numbers = list('0123456789') # Create a list of digits from 0 to 9
    random.shuffle(numbers) # Shuffle them into random order

    # Get the first NO_OF_DIGITS digits in the list for the secret number
    for i in range(NO_OF_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

if __name__ == "__main__":
    main()