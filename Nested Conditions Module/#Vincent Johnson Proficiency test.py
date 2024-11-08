#Vincent Johnson Proficiency test
'''
INSTRUCTIONS:
Create a multiple choice quiz game that tests the user's knowledge on a topic (please pick a school appropriate topic and yes all of the questions need to be on that topic!) 

Give the user 5 multiple choice questions with A, B, C,  and D options for the user to select from. Use a nested conditional to check if the users answer if correct AND keep score so they can see how well they did at the end of the quiz.

After each question you need to tell the user if they were right or wrong. 

If the user got the question wrong they should be given an easier question to answer next. 
'''
import random
wins = 0
rounds = 0
qst = "Which of these colours is most commonly neon?\nA: Beige\nB: Teal\nC: Jade\nD: Yellow"
qstans = "d"

def main(wins, rounds, qst, qstans):
    print(f"{qst}")
    ans = input("What is your answer?\n")
    ans = ans.lower()
    if ans == qstans:
        wins +=1
        rounds +=1
        print(f"{wins}/{rounds}")
        option = random.randint(5,9)
    else:
        wins +=0
        rounds +=1
        print(f"{wins}/{rounds}")
        option = random.randint(1,4)
    if option < 6:
        if option == 1:
            qst = "What colour of these provokes the emotion happiness?\nA: Yellow\nB: Dark Blue\nC: Black\nD: Blood Red"
            qstans = "a"
            main(wins, rounds, qst, qstans)
        elif option == 2:
            qst = "Which of these colours is the most common favourite?\nA: Black\nB: Orange\nC: Blue\nD: Red"
            qstans = "c"
            main(wins, rounds, qst, qstans)
        elif option == 3:
            qst = "Which colour is most prevelant in sunsets?\nA: Purple\nB: Orange\nC: Blue\nD: Black"
            qstans = "b"
            main(wins, rounds, qst, qstans)
        elif option == 4:
            qst = "Which colour is most commonly associated with rain?\nA: Purple\nB: Blue\nC: Grey\nD: Black"
            qstans = "b"
            main(wins, rounds, qst, qstans)
    else:
        if option == 5:
            qst = "Which of these colours do not evoke peace?\nA: Yellow\nB: Dark Blue\nC: Green\nD: Purple"
            qstans = "a"
            main(wins, rounds, qst, qstans)
        elif option == 6:
            qst = "Which of these colours cannot be seen well by most colourblind people?\nA: Black\nB: Any\nC: Green\nD: Red"
            qstans = "c"
            main(wins, rounds, qst, qstans)
        elif option == 7:
            qst = "Which colour is not actually a colour?\nA: Alizarin\nB: Dorno\nC: Apricot\nD: Beaver"
            qstans = "b"
            main(wins, rounds, qst, qstans)
        elif option == 8:
            qst = "Which of these colours is a shade of green?\nA: Catawba\nB: Camel\nC: Celadon\nD: Celeste"
            qstans = "b"
            main(wins, rounds, qst, qstans)
        elif option == 9:
            qst = "Which colour is most commonly associated with rain?\nA: Purple\nB: Blue\nC: Grey\nD: Black"
            qstans = "b"
            main(wins, rounds, qst, qstans)
main(wins, rounds, qst, qstans)            