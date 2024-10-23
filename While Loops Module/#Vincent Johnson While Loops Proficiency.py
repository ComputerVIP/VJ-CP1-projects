#Vincent Johnson While Loops Proficiency test
import random

score = 0
games = 0

def rps(score, games):
    ans = int(input("Do you want to continue playing? y=1/n=2\n"))
    if ans == 1:
        ans = True
    elif ans == 2:
        print("Thanks for playing!")
        ans = False
    while ans == True:
        choice = int(input("Press 1 for paper\nPress 2 for rock\nPress 3 for scissors\n"))
        other = random.randint(1,3)
        if choice == 1:
            if other == 2:
                score += 1
                games += 1
                print("\nYou win!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 1:
                games += 1
                print("\nYou tied!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 3:
                games += 1
                print("\nYou lost!")
                print(f"{score}/{games}")
                rps(score, games)
        elif choice == 2:
            if other == 3:
                score += 1
                games += 1
                print("\nYou win!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 2:
                games += 1
                print("\nYou tied!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 1:
                games += 1
                print("\nYou lost!")
                print(f"{score}/{games}")
                rps(score, games)
        elif choice == 3:
            if other == 1:
                score += 1
                games += 1
                print("\nYou win!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 3:
                games += 1
                print("\nYou tied!")
                print(f"{score}/{games}")
                rps(score, games)
            elif other == 2:
                games += 1
                print("\nYou lost!")
                print(f"{score}/{games}")
                rps(score, games)
rps(score, games)