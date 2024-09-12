#Vincent Johnson
#INSTRUCTIONS:
#Write a program that takes in grades for each of your classes and then outputs for the user their average grade.

list = (" ")

x = 0
cls = int(input("How many classes do you have?"))
while x != cls:
    x += 1
    list = list+",",str(input(f"What's the letter grade of your {x} class?"))
    if x == cls:
        A = list.count("A")
        B = list.count("B")
        C = list.count("C")
        D = list.count("D")
        F = list.count("F")
        if A>F:
            if A>D:
                if A>C:
                    if A>B:
                        print("Your average grade is an A.")
        if B>F:
            if B>D:
                if B>C:
                    if B>A:
                        print("Your average grade is a B.")
        if C>F:
            if C>D:
                if C>B:
                    if C>A:
                        print("Your average grade is a C.")