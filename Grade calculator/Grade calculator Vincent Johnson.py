#Vincent Johnson
#INSTRUCTIONS:
#Write a program that takes in grades for each of your classes and then outputs for the user their average grade.

list = (" ")

x = 0
cls = int(input("How many classes do you have?\n"))
while x != cls:
    x += 1
    list = list+str(input(f"What's the letter grade of your {x} class?\n"))
    if x == cls:
        A = list.count("A")
        A2 = list.count("A-")
        B2 = list.count("B+")
        B = list.count("B")
        B3 = list.count("B-")
        C2 = list.count("C+")
        C = list.count("C")
        C3 = list.count("C-")
        D2 = list.count("D+")
        D = list.count("D")
        D3 = list.count("D-")
        F = list.count("F")
        if A>F:
            if A>D3:
                if A>D:
                    if A>D2:
                        if A>C3:
                            if A>C:
                                if A>C2:
                                    if A>B3:
                                        if A>B:
                                            if A>B2:
                                                if A>A2:
                                                    print("Your average grade is an A.")
                                                    break
        if A2>F:
            if A2>D3:
                if A2>D:
                    if A2>D2:
                        if A2>C3:
                            if A2>C:
                                if A2>C2:
                                    if A2>B3:
                                        if A2>B:
                                            if A2>B2:
                                                if A2>A:
                                                    print("Your average grade is an A-.")
                                                    break
        if B2>F:
            if B2>D3:
                if B2>D:
                    if B2>D2:
                        if B2>C3:
                            if B2>C:
                                if B2>C2:
                                    if B2>B3:
                                        if B2>B:
                                            if B2>A2:
                                                if B2>A:
                                                    print("Your average grade is a B+.")
                                                    break
        if B>F:
            if B>D3:
                if B>D:
                    if B>D2:
                        if B>C3:
                            if B>C:
                                if B>C2:
                                    if B>B3:
                                        if B>B2:
                                            if B>A2:
                                                if B>A:
                                                    print("Your average grade is a B.")
                                                    break
        if B3>F:
            if B3>D3:
                if B3>D:
                    if B3>D2:
                        if B3>C3:
                            if B3>C:
                                if B3>C2:
                                    if B3>B:
                                        if B3>B2:
                                            if B3>A2:
                                                if B3>A:
                                                    print("Your average grade is a B-.")
                                                    break
        if C2>F:
            if C2>D3:
                if C2>D:
                    if C2>D2:
                        if C2>C3:
                            if C2>C:
                                if C2>B2:
                                    if C2>B3:
                                        if C2>B:
                                            if C2>A2:
                                                if C2>A:
                                                    print("Your average grade is a C+.")
                                                    break
        if C>F:
            if C>D3:
                if C>D:
                    if C>D2:
                        if C>C3:
                            if C>C2:
                                if C>B3:
                                    if C>B:
                                        if C>B2:
                                            if C>A2:
                                                if C>A:
                                                    print("Your average grade is a C.")
                                                    break
        if C3>F:
            if C3>D3:
                if C3>D:
                    if C3>D2:
                        if C3>C:
                            if C3>C2:
                                if C3>B3:
                                    if C3>B:
                                        if C3>B2:
                                            if C3>A2:
                                                if C3>A:
                                                    print("Your average grade is a C-.")
                                                    break
        if D2>F:
            if D2>D3:
                if D2>D:
                    if D2>C3:
                        if D2>C:
                            if D2>C2:
                                if D2>B2:
                                    if D2>B3:
                                        if D2>B:
                                            if D2>A2:
                                                if D2>A:
                                                    print("Your average grade is a D+.")
                                                    break
        if D>F:
            if D>D3:
                if D>D2:
                    if D>C3:
                        if D>C:
                            if D>C2:
                                if D>B3:
                                    if D>B:
                                        if D>B2:
                                            if D>A2:
                                                if D>A:
                                                    print("Your average grade is a D.")
                                                    break
        if D3>F:
            if D3>D:
                if D3>D2:
                    if D3>C3:
                        if D3>C:
                            if D3>C2:
                                if D3>B3:
                                    if D3>B:
                                        if D3>B2:
                                            if D3>A2:
                                                if D3>A:
                                                    print("Your average grade is a D-.")
                                                    break
        if F>D3:
            if F>D:
                if F>D2:
                    if F>C3:
                        if F>C:
                            if F>C2:
                                if F>B3:
                                    if F>B:
                                        if F>B2:
                                            if F>A2:
                                                if F>A:
                                                    print("Your average grade is a F.")
                                                else:
                                                    print("No average grade.")
                                            else:
                                                print("No average grade.")
                                        else:
                                            print("No average grade.")
                                    else:
                                        print("No average grade.")
                                else:
                                 print("No average grade.")
                            else:
                                print("No average grade.")
                        else:
                            print("No average grade.")
                    else:
                        print("No average grade.")
                else:
                    print("No average grade.")
            else:
                print("No average grade.")
        else:
            print("No average grade.")