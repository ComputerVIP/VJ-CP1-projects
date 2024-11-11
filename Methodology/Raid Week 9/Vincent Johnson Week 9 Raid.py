#Vincent Johnson Week 9 Raid
import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while game_over != True: #This used not, logic error, just makes some weird comparisons
        guess = int(input("Enter your guess: ")) #This was made a str and not int, needs to be int for comparisons, just syntax error
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            attempts +=1 #Guesses was not added to, simple logic error, this made it so you can guess infinitely
            print("Too high! Try again.")
        elif guess < number_to_guess:
            attempts += 1 #Guesses was not added to, simple logic error, this made it so you can guess infinitely
            print("Too low! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
    return #Did not actually end when Game Over is reached, logic error
start_game()