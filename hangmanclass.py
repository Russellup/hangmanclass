import random
man_hanging = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
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
wordlist = 'garrapolo, rice, williams, kittle '.split()




class Hangman:
    

  def __init__(self):
       	

     def choose_word(self):
         word_index = random.randint(0,len(wordlist)-1)
         return wordlist[word_index]
     
     def print_word_dashes(missed_letters, correct_letters, hidden_word):
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




    