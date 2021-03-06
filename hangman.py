import random
pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
listoptions = {'animal':['monkey' , 'panda', 'shark', 'zebra', 'gorilla', 'walrus', 'leopard', 'wolf', 'antelope' ,'eagle','jellyfish','crab','giraffe','woodpecker','camel','starfish','koala','alligator','owl','tiger','bear'],
               'food':['cookies', 'icecream','pizza', 'burger', 'taco','spaghetti','pasta','burritos','salad','smoothie','yogurt', 'cereal','cake','bread','meat', 'eggs','pancakes','pie','muffin','cheese','chips','bagel', 'fruit'],
               'school':['backpack','pencil', 'whiteboard', 'marker', 'answer','book', 'binder','crayon','computer','classroom','test','gym','grades','homework','history','math','english','science','library','learn','notebook','paper']}


#gets word by inputing array and returning secret word
def getWord(secDict):
    wordkey = random.choice(list(secDict.keys()))
    wordIndex = random.randint(1, len(wordkey)-1)
    return [secDict[wordkey][wordIndex], wordkey]


#will show blanks, missed letters, correct letters, and figure
def board(figure, missed, correct, secret_word):
    print(figure[len(missed)])

    print('Missed Letters: ')
    for letter in missed:
        print( letter)

        
    blanks = list(('_' * len(secret_word)))

    #print(blanks)

    for i in range(0, len(blanks)):
        if secret_word[i] in correct:
            blanks[i] = secret_word[i]
            #correct.append(guess)
        #else:s
            #missed.append(guess)
    emptystr = ""
    emptystr= emptystr.join(blanks)
    print("Your Guesses! = " + emptystr + '\n')
    return emptystr
    #print(blanks)



def getGuess(alreadyGuessed):
    #print('Guess a letter')
    while True:
        guess = input('Guess a letter ')
        guess = guess.lower()
        if guess in alreadyGuessed:
            print('You have already guessed this. Please pick a different letter')
        elif len(guess) != 1:
             print('Enter ONE letter')
        elif guess not in 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z':
            print('enter a LETTER')
        else:
            break
    return guess



def mssg1(winorlose):
    print('''
----------------------------------
GAME OVER!!!

''' + winorlose + '''

------------------------------------

    ''')


def playagain():
    while True:
        wanna = input('Would you like to play again? (y/n) ')
        wanna = wanna.lower()
        if len(wanna) != 1:
            print('Pick one please.')
        elif wanna not in 'y,n':
            print('Please enter "y" or "n".')
        else:
            break
    if wanna == 'y':
        return True
    elif wanna == 'n':
        return False



# Call everything in a while loop and then call again in a loop
while True:

    word, key = getWord(listoptions)
    wrong = []
    right = []

    gameDone = False

    while True:
        print("The word is '"+ key + "' related.")
        board(pics, wrong, right, word)

        if len(wrong) == len(pics) - 1:
            yay = 'You Looose!!! :( the word was ' + word
            gameDone = True

        if gameDone:
            mssg1(yay)
            break

        guessedLetter = getGuess(wrong + right)
        correctCount = 0

        if guessedLetter in word:
            right.append(guessedLetter)

            for i in range(len(word)):
                if word[i] in right:
                    correctCount += 1
                    #print(correctCount)
                    #print(len(word))


        else:
            wrong.append(guessedLetter)

        if correctCount == len(word):
            yay = 'You Win !!!! :-)'
            gameDone = True

    if not playagain() :
        break






            

    


    
           
          
          
