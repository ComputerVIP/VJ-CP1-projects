#Vincent Johnson assignment


def reg():
    print("\n---Note, this version can only save 2 numbers in an expression---\n")
    line = input("What is the expression? (Quick note, multiplication is *, rounding is ~, division is /, and exponent is ^)\n")
    parts = line.split("%")
    part = line.split("*")
    pars = line.split("/")
    pas = line.split("^")
    pats = line.split("~")
    if "/0" in line:
        print("You cannot divide by 0!")
        return
    elif "/ 0" in line:
        print("You cannot divide by 0!")
        return
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
reg()