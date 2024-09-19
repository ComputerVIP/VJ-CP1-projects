print("\n---All of these questions MUST start with a capital letter---\n")
score = 0
cnt = 0

ans = input("Ready to begin? There are 5 questions. Yes/No \n")


if ans == "Yes":
    qst1 = input("\n1. What language is this?\nprint('Hello World!')\n")
    if qst1 == "Python":
        score += 1
        cnt += 1
        print(f"\nCorrect! You are {score}/{cnt}")
    else:
        cnt += 1
        print(f"\nIncorrect! You are {score}/{cnt}")

    qst2 = input("\n2. Where is UCAS (9th-10th) located?\n")
    if qst2 == "Provo":
        score += 1
        cnt += 1
        print(f"\nCorrect! You are {score}/{cnt}")
    else:
        cnt += 1
        print(f"\nIncorrect! You are {score}/{cnt}")
    
    qst3 = input("\n3. How many questions are there?\n")
    if qst3 == "5":
        score += 1
        cnt += 1
        print(f"\nCorrect! You are {score}/{cnt}")
    else:
        cnt += 1
        print(f"\nIncorrect! You are {score}/{cnt}")
    
    qst4 = input("\n4. Is HTML a programming language?\n")
    if qst4 == "No":
        score += 1
        cnt += 1
        print(f"\nCorrect! You are {score}/{cnt}")
    else:
        cnt += 1
        print(f"\nIncorrect! You are {score}/{cnt}")
    
    qst5 = input("\n5. Was this made in a class for a class?\n")
    if qst5 == "Yes":
        score += 1
        cnt += 1
        print(f"\nCorrect! You are {score}/{cnt}")
    else:
        cnt += 1
        print(f"\nIncorrect! You are {score}/{cnt}")
    if cnt == 5:
        print(f"\n---Your total score was {score} out of {cnt}!---\n")