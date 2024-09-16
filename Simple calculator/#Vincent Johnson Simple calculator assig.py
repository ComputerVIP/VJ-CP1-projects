#Vincent Johnson Simple calculator assignment
#INSTRUCTIONS:
#Build a simple calculator that will perform all arithmetic operations for 2 numbers inputted by the user. (I do want you to include modulo, exponents and rounded division)
line = ("")
numbers = []

def reg():
    print("\n---Note, this version can only save 2 numbers in an expression---\n")
    line = input("What is the expression? (Quick note, multiplication is *, rounding is RND, and exponent is ^)\n")
    parts = line.split("%")
    parts = line.split("*")
    parts = line.split("/")
    parts = line.split("^")
    parts = line.split("rnd")
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
            num1 = int(parts[0].strip()) 
            num2 = int(parts[1].strip())
        
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        except:
            print("Failed multiplication")
    if "/" in line:
        try:
            num1 = int(parts[0].strip()) 
            num2 = int(parts[1].strip())
        
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        except:
            print("Failed division")
    if "^" in line:
        try:
            num1 = int(parts[0].strip()) 
            num2 = int(parts[1].strip())
        
            result = num1 ** num2
            print(f"The result of {num1} ^ {num2} is: {result}")
        except:
            print("Failed exponent")
    if "rnd" in line:
        try:
            num1 = int(parts[0].strip()) 
            num2 = int(parts[1].strip())
        
            result = round(num1)
            print(f"The result of {num1} rounded is: {result}")
        except:
            print("Failed rounding")




def syn():
    import sympy

    line = (input("What is the expression? (% is modulo, ** is exponent, round()is round.)\n"))
    anl = sympy.sympify(line)
    print ((f"\n\n---Your equation, {line} equates to: {anl}---\n\n"))

tel = ("")

ans = input ("Sympy y/n?\n")
if ans == ("y"):
    print("---NOTE: To run this program you will have to run pip install sympy---\n")
    tel = input("Do you have Sympy installed? y/n\n")
    if tel == ("y"):
        syn()
else:
    reg()