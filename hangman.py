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
    for i in range(0, len(word)):
        if letter == word[i]:
            guessArray[i] = letter

def checkWin(guessArray):
    for i in range(0, len(guessArray)):
        if guessArray[i] == "_":
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

    guess 