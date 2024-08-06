from words import wordList
import random

def get_word():
    word = random.choice(wordList)
    return word.upper()

def play(word):
    wordCompletion = '_' * len(word)
    guessed = False
    guessedLetters = []
    guessedWords = []
    tries = 6
    print("Let's Play Hangman!")
    print(displayHangman(tries))
    print(wordCompletion)
    print('\n')
    while not guessed and tries > 0:
        guess = input('Please guess a letter or word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessedLetters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessedLetters.append(guess)
            else:
                print('Good job', guess, "is in the word!")
                guessedLetters.append(guess)
                wordAsList = list(wordCompletion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    wordAsList[index] = guess
                wordCompletion = "".join(wordAsList)
                if "_" not in wordCompletion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessedWords:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessedWords.append(guess)
            else:
                guessed = True
                wordCompletion = word
        else:
            print('Not a valid guess.')

        print(displayHangman(tries))
        print(wordCompletion)
        print('\n')
    if guessed:
        print('Congrats, you guess the word! You Win!')
    else:
        print("You lose, the word was", word)

def displayHangman(tries):
    stages = [  """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / \\
                    -
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      / 
                    -
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|/
                    |       |
                    |      
                    -
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      \|
                    |       |
                    |      
                    -
                """,
                """
                    ---------
                    |       |
                    |       O
                    |       |
                    |       |
                    |      
                    -
                """,
                """
                    ---------
                    |       |
                    |       O
                    |      
                    |       
                    |      
                    -
                """,
                """
                    ---------
                    |       |
                    |      
                    |      
                    |      
                    |      
                    -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play Again> (y / n)\n").lower() == 'y':
        word = get_word()
        play(word)

# Running Program by running Script on command line
if __name__ == '__main__':
    main()