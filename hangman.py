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

    return True

def checkWin(guessArray):
    print("here")
    for i in range(0, len(guessArray)):
        if guessArray[i] == "_":
            print("here")
            return False
    
    return True
guessArray = []

#chosenWord = chooseWord()
chosenWord = "molly"
word = []
game = True

for i in range(0, len(chosenWord)):
    guessArray.append("_")
    word.append(chosenWord[i])

while game:

    printWord(guessArray)

    guess = input("what letter would you like to guess: ").lower()

    checkLetter(word, guessArray, guess)

    if checkWin:
        game = False


print("you won!")