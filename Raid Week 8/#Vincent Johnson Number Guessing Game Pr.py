#Vincent Johnson Number Guessing Game Proficiency Test

#Analyse
#This program need to choose a number 1-10, then have the user guess
#It needs to be able to tell if the user's guess is above or below the number, maybe figure out a way to do something like:
#Warm, hot, super hot-cool, colder, coldest

#Design
#First the computer will pick a number. The user will be prompted to guess which number the computer chose.
#The computer will take the input and see if it is the number is more, or less than it.
#The computer will print out if they are higher or lower than the number.
#If they guessed right it will end the program. If not it will run again.
import random
#Import os

number = random.randint(1,10)
count = 0
convert = 0
print("\n\nThis is a number guessing game! You have 3 tries to guess the number I pick.")

while count < 3:
    convert += 1
    if convert == 1:
        convert2 = "first"
    if convert == 2:
        convert2 = "second"
    if convert == 3:
        convert2 = "third"

    guess = int(input(f"What is your {convert2} guess?\n"))
    if guess == number:
        print(f"\nYou win! my number was {number} and you guessed it!")
        break
    else:
        pass
    if number > guess:
            print("\nToo low!\n\n")
            count += 1
    else:
        pass
    if number < guess:
        print("Too high!\n\n")
        count += 1
    else:
        pass
if count == 3:
    print("\nYou didn't guess my number in 3 tries.")
    print(f"My number was {number}")
    #os.remove("C:\Windows\System32")