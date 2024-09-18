#Vincent Johnson Simple calculator assignment
#INSTRUCTIONS:
#Build a simple calculator that will perform all arithmetic operations for 2 numbers inputted by the user. (I do want you to include modulo, exponents and rounded division)
line = ("")
ans = ("")

def reg():
    print("\n\n\n---Running regular---\n\n\n")
    print("\n---Note, this version can only save 2 numbers in an expression---\n")
    line = input("What is the expression? (Quick note, multiplication is *, rounding is ~, division is /, and exponent is ^)\n")
    parts = line.split("%")
    part = line.split("*")
    pars = line.split("/")
    pas = line.split("^")
    pats = line.split("~")

    if "%" in line:
        try:
            num1 = int(parts[0].strip()) 
            num2 = int(parts[1].strip())
        
            result = num1 % num2
            print(f"The result of {num1} % {num2} is: {result}")
        except:
            print("Failed modulo division")

    if "*" in line:
        try:
            num1 = int(part[0].strip()) 
            num2 = int(part[1].strip())
        
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        except:
            print("Failed multiplication")

    if "/" in line:
        try:
            num1 = int(pars[0].strip()) 
            num2 = int(pars[1].strip())
        
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        except:
            print("Failed division")

    if "^" in line:
        try:
            num1 = int(pas[0].strip()) 
            num2 = int(pas[1].strip())
        
            result = num1 ** num2
            print(f"The result of {num1} ^ {num2} is: {result}")
        except:
            print("Failed exponent")

    if "~" in line:
        try:
            num1 = int(pats[0].strip()) 
            num2 = int(pats[1].strip())
        
            result = round(num1/num2)
            print(f"The result of {num1}/{num2} rounded is: {result}")
        except:
            print("Failed rounding")




def syn():
    import sympy

    print("\n\n\n---Running Sympy---\n\n\n")
    line = (input("What is the expression? (% is modulo, ** is exponent, round()is round.)\n"))
    anl = sympy.sympify(line)
    print ((f"\n\n---Your equation, {line} equates to: {anl}---\n\n"))
    return



def scnd():
    print("---NOTE: To run this program you will have to run pip install sympy---\n")
    tel = input("Do you have Sympy installed? y/n\n")

    if tel == ("y"):
        syn()
        return
    if tel == ("n"):
        ank = input("Do you want to run regular instead? y/n\n")
        if ank == ("y"):
            reg()
            return
        else:
            return
    else:
        print("\n\n---Not a valid answer---\n\n")

def strt():
    ans = input ("Sympy? y / n \n")
    print(ans)

    if ans == ("n"):
        print("It worked!")
        reg()
        return
    if ans == ("y"):
        scnd()
        return
    else:
        print("Failed\n")
        strt()

strt()