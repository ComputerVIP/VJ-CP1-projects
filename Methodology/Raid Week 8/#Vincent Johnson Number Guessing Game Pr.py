#Vincent Johnson Number Guessing Game Proficiency Test

'''
Analyse:
This program need to choose a number 1-10, then have the user guess
It needs to be able to tell if the user's guess is above or below the number, maybe figure out a way to do something like:
Warm, hot, super hot-cool, colder, coldest


Design:
First the computer will pick a number. The user will be prompted to guess which number the computer chose.
The computer will take the input and see if it is the number is more, or less than it.
The computer will print out if they are higher or lower than the number.
If they guessed right it will end the program. If not it will run again.

Testing:
    Gabe:
        Yes the program ran for him.
        He did guess a number and my if-then-else logic freaked.
        He was able to use it without my explanation.
    Seth:
        Yes the program ran for him as well.
        My if-then-else logic freaked for him too.
        He was able to use it without my explanation.


Improvements:
I was not able to get the close-to check working, maybe try for that again
Make the text look nicer, not very good in it's stage right now
Maybe make it more streamline, not neccesary to use words for numbered guess
'''

import random
#Import os


number = random.randint(1,10)
#Picks a random number for person to guess
count = 0
#Count of how many tries you've done
convert = 0
#Just a code to convert numbers into words
print("\n\nThis is a number guessing game! You have 3 tries to guess the number I pick.")


while count < 3:
    #While the number of times played is less than 3

    convert += 1
    if convert == 1:
        convert2 = "first"
    if convert == 2:
        convert2 = "second"
    if convert == 3:
        convert2 = "third"
    #This all just converts numbers to words for prompt


    guess = int(input(f"What is your {convert2} guess?\n"))
    #This takes the user's guess for the number

    if guess == number:
        #If they guessed the number the computer chose
        print(f"\nYou win! my number was {number} and you guessed it!")
        break
    else:
        pass

    if number > guess:
        #If their guess was too low
            print("\nToo low!\n\n")
            count += 1
    else:
        pass

    if number < guess:
        #If their guess was too high
        print("Too high!\n\n")
        count += 1
    else:
        pass

if count == 3:
    #If they couldn't guess the number in three tries
    print("\nYou didn't guess my number in 3 tries.")
    print(f"My number was {number}")
    #os.remove("C:\Windows\System32")
