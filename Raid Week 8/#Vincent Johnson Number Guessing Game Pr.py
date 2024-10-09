#Vincent Johnson Number Guessing Game Proficiency Test

#Analyse
#This program need to choose a number 1-10, then have the user guess
#It needs to be able to tell if the user's guess is above or below the number, maybe figure out a way to do something like:
#Warm, hot, super hot-cool, colder, coldest

#Design
#First the computer will pick a number. The user will be prompted to guess which number the computer chose.
#The computer will take the input and see if it is the number it chose, more, or less than it.
#The computer will print out if they are close, far, or if they got the number.
#If they guessed right it will end the program. If not it will run again.
import random
#Import os

while True:
    number = random.int(1,10)
    print("This is a number guessing game! You have 3 tries to guess the number I pick.")
    guess = int(input("What is your first guess?\n"))
    if guess == number:
        print(f"You win! my number was: {number} and you guessed it!")
    else:
        print("Not quite!")