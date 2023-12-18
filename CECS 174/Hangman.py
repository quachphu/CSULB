#music downloaded from www.zapsplat.com/
wordlist = ["Success", "positive", "attitude"]
#Step1-Randomly choose a word from the list and assign it to variable chosenWord
#Step2- Ask the user to guess a letter guess= input() make sure guess is lower case
#Step3- check if guess is one of the letters in chosenWord

#Step1-Randomly choose a word from the list and assign it to variable chosenWord
import random
import sys
import colorama
from colorama import Fore

print(Fore.RED + 'This text is red in color')

'''print("\033[1;32;40m Bright Green  \n")

ANSI escape code format
\033[Escape code, this is always the same
1 = Style, 1 for normal.
32 = Text color, 32 for bright green.
40m = Background color, 40 is for black.'''
print("Normal")
print("\033[0;30;48m Black")
print("\033[1;31;48m Red")
print("\033[2;32;48m Green")
print("\033[3;33;48m Yellow")

HANGMAN_PICS = ['''
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

wordlist = ["apple", "banana", "success", "positive"]
#theWord = choose a random word
#challenge: write the choice function
#Ask user to guess a letter
#Check if the letter guess is one of the letters in theWord
computerWord = random.choice(wordlist)
print(f"The computer's word is {computerWord}.. this is for testing purpose remove when playing ")
#in order to compare lower cases only convert everything to lower
'''for letter in computerWord:
    print ("_", end=" ")
print()'''
guess = input("Guess a letter ").lower()
#can remove
'''for letter in computerWord:
    if guess == letter:
        print ("Correct")
    else:
        print("Wrong")'''

'''for letter in computerWord:
    if guess == letter:
        print (letter, end=" ")
    else:
        print("_", end=" ")
print()'''
outWord =""
for letter in computerWord:
    if guess == letter:
        outWord +=letter
    else:
        outWord +=" _ "
print("String", outWord)
outList =[]
for letter in computerWord:
    if guess == letter:
        outList.append(letter)
    else:
        outList.append("_")
print("list ", outList)




'''for i in range(len(computerWord)):
    guess = input("Guess a letter ").lower()

    #Show if we use output only without saving
    for letter in computerWord:
        if guess == letter:
            print (letter, end=" ")
        else:
            print("_", end=" ")
    print()'''

#print("The list.... if the letter appears more than once it does not ")
outList =[]
for i in range(len(computerWord)):
    outList.append("_")
letterLeft = len(computerWord)
'''for i in range(len(computerWord)):
    guess = input("Guess a letter ").lower()
    #for i in range(len(computerWord)):
    j = 0
    for letter in computerWord:
        if guess == letter:
                outList[j] = letter
        j +=1
    print("list ", outList)'''
#Solved without lives
'''i = 0
while i < len(computerWord) and letterLeft>0 :
    guess = input("Guess a letter ").lower()
    #for i in range(len(computerWord)):
    j = 0
    for letter in computerWord:
        if guess == letter:
                outList[j] = letter
                letterLeft -=1
        j +=1
    i +=1
    print("list ", outList)'''
#if letter is repeated it will give wrong results
'''i = 0 #to parse each letter
live = 0 #to determine which image to output
lives = len(HANGMAN_PICS)
while i < len(computerWord)+len(HANGMAN_PICS) and letterLeft>0 and lives:
    guess = input("Guess a letter ").lower()
    flag = False
    #for i in range(len(computerWord)):
    j = 0   #needed to determine the index of the correct letter
    for letter in computerWord:
        if guess == letter:
            outList[j] = letter
            letterLeft -=1
            flag = True
        #Natural thought else lives
        j +=1
    i +=1
    if flag:
        print("list ", outList)
    else:
        print(HANGMAN_PICS[live])
        live += 1
        lives -=1
if letterLeft > 0:
    print(":-(")
else:
    print(":-)")'''
import pygame
#pygame.mixer.init(44100, -16,2,2048)
pygame.init()
errorSound = pygame.mixer.Sound('error.mp3')
correctSound = pygame.mixer.Sound('win.mp3')
pygame.mixer.music.load('error.mp3')
#pg.mixer.music.play(-1, 0.0)
pygame.mixer.music.play(1)

musicPlaying = True
######problem when s is entered twice, it will write it in the wrong place
#pg.mixer.music.stop()
i = 0 #to parse each letter
live = 0 #to determine which image to output
lives = len(HANGMAN_PICS)
while i < len(computerWord)+len(HANGMAN_PICS) and letterLeft>0 and lives:
    guess = input("Guess a letter ").lower()
    flag = False
    #for i in range(len(computerWord)):
    j = 0   #needed to determine the index of the correct letter
    for letter in computerWord:
        if guess == letter:
            pygame.mixer.Sound.play(correctSound)
            flag = True
            if outList[j] == "_":
                outList[j] = letter
                letterLeft -=1
                #flag = True
            else:
                #print("repeated letter, round not counted")
                i -=1
                continue
                #flag = True
        j +=1
    i +=1
    if flag:
        print("list ", outList)
    else:
        print(HANGMAN_PICS[live])
        pygame.mixer.Sound.play(errorSound)
        live += 1
        lives -=1
if letterLeft > 0:
    print(":-(")
else:
    print(":-)")