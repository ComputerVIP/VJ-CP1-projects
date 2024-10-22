#Vincent Johnson While Loops Proficiency test
score = 0
games = 0

def rps():
    ans = input("Do you want to continue playing? y/n\n")
    if ans is "y":
        ans = True
    if ans is "n":
        ans = False
    else:
        print("That is not a valid answer! y/n!")
        rps()
    while ans != True: