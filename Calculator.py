import math 
def calc(): 
    print("\n") 
    number = input("What's the math problem?\n math.sqrt square root\n ** exponent\n * multiply\n / divide\n math.fabs absolute value\n math.factorial factorial\n math.gcd greatest common denominator\n math.lcm lowest common multiple\n\n")
    try: 
        result = eval(number)
        print(f"--The equation is: {number}--\n --The answer is: {result}--\n")
        print("Visit https://docs.python.org/3/library/math.html for more info on math library.")
    except: 
        print("--Not valid equation--\n")
        print("Visit https://docs.python.org/3/library/math.html for more info on math library.")
        calc()
        
    
calc()