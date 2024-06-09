import random

def chooseWord():
    words = ["wish", "frozen", "molly"]
    
    chosenWord = words[random.randrange(0,len(words))]
    return chosenWord
    
def printWord(wordArr):
    for letter in wordArr:
        print(letter, end=" ")
    print()
    
def checkLetter(word, guessArray, letter):
    correctGuess = False
    for i in range(0, len(word)):
        if letter == word[i]:
            guessArray[i] = letter
            correctGuess = True

            print("Correct Guess!")

    return correctGuess

def checkWin(guessArray):
    for i in range(0, len(guessArray)):
        if guessArray[i] == "_":
            return False
    
    return True

LIVES = 6

# create lists and variables
guessArray = []
chosenWord = chooseWord()
word = []
game = True
currentLives = LIVES



for i in range(0, len(chosenWord)):
    guessArray.append("_")
    word.append(chosenWord[i])

while game:

    printWord(guessArray)

    print(f"you have {currentLives} lives left")

    guess = input("what letter would you like to guess: ").lower()

    correctGuess = checkLetter(word, guessArray, guess)

    if correctGuess == False:
        currentLives -= 1

    if checkWin(guessArray):
        print("you won!")
        game = False

    # check loss
    if currentLives <= 0:
        print("you lost")
        game = False
