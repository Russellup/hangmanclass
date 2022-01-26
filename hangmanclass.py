import random
man_hanging = ['''
     +---+
         |
         |
         |
        ===''', '''
    #  +---+
     O   |
         |
         |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

class Hangman:
    def __init__(self):
        self.wordlist = ['garrapolo', 'rice', 'williams', 'kittle'] 
        self.turns = 12 
        self.guesses = ''
    
    def choose_word(self): #self refers to the object Hangman
         word_index = random.randint(0,len(self.wordlist)-1)
         self.hidden_word = self.wordlist[word_index]#dotnotation accesses the attributes and methods
         #of each method of instances of different object classes. 
         # object instance. attributes and methods, accesses methods in class with
         #  object of a class in format
         return self.hidden_word
     
    def print_word_dashes(missed_letters, correct_letters, hidden_word): #<- instance variable
        print(man_hanging[len(missed_letters)])
        print()
        print('Missed letters', end='')
        for letter in missed_letters:
            print(letter, end='')
        print()

        blanks = '_' * len(hidden_word)

        for i in range(len(hidden_word)):
            if hidden_word[i] in correct_letters:
                blanks = blanks[:i] + hidden_word[i] + blanks[i+1:]

        for letter in blanks:
            print(letter, end='')
        print()                
    
    def getguess(alreadyGuessed):
         while True:
          print('Guess a letter.')
          guess = input()
          guess = guess.lower()
          if len(guess) != 1:
              print('Please enter a single letter.')
          elif guess in alreadyGuessed:
              print('You have already guessed that letter. Choose again.')
          elif guess not in 'abcdefghijklmnopqrstuvwxyz':
              print('Please enter a LETTER.')
          else:
              return guess


    def run(self):
        print('rocks')
        print('self.turns',self.turns)
        while self.turns > 0:
            failed = 0
            for char in self.hidden_word:
                if char in self.guesses:
                    print(char)
                else:
                    print("_")
                    failed += 1
                    
                if failed == 0:
                    print("You Win")
                    print("The word is: ", self.hidden_word)
                    break
            guess = input("guess a character:")
            self.guesses += guess
            if guess not in self.hidden_word:
                self.turns -= 1
                print("Wrong")
                print("You have", + self.turns, 'more guesses')
            if self.turns == 0:
                    print("You Lose")



# print('H A N G M A N')
# missedLetters = ''
# correctLetters = ''
# secretWord = getRandomWord(words)
# gameIsDone = False
 
# while True:
#         displayBoard(missedLetters, correctLetters, secretWord)
 
      
    # guess = getGuess(missedLetters + correctLetters)
 
    # if guess in secretWord:
    #       correctLetters = correctLetters + guess
 
         
    #       foundAllLetters = True
    #       for i in range(len(secretWord)):
    #          if secretWord[i] not in correctLetters:
    #              foundAllLetters = False
    #              break
    #          if foundAllLetters:
    #           print('Yes! The secret word is "' + secretWord +
    #                '"! You have won!')
    #          gameIsDone = True
    #       else:
    #        missedLetters = missedLetters + guess

         
    #       if len(missedLetters) == len(HANGMAN_PICS) - 1:
    #         displayBoard(missedLetters, correctLetters, secretWord)
    # print('You have run out of guesses!\nAfter ' +
    #                str(len(missedLetters)) + ' missed guesses and ' +
    #                str(len(correctLetters)) + ' correct guesses',
    #                the word was "' + secretWord + '"')
    #          gameIsDone = True
h1 = Hangman() #variable assignment
print(h1.choose_word())
h1.run() 
#calling split method of string which evaluates to  list 
# passing list to a call of choose word, your passing the result of that call to print  
#nested
print(h1.hidden_word) #printing attributes of a object 
h2 = Hangman()
print(h2.choose_word())
print(h2.hidden_word)
#pass in the wordlist twice although needs to be changed, passs first when creating
#  object then pass again when calling chooseword we want to reduce that we 
# want to not repeat, so we want to get rid of passing in the wordlist a second time

 

    
