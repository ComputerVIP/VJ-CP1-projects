import sympy

def maph2(eqtn):
    print("Running maph2")

    x = 0
    y = 0
    while True:
        #Thinking of taking out the number before and after ^ to eval them seperately
        result = sympy.sympify(eqtn.replace('x', str(x)).replace('y', str(y)))
        if result is True:
            print(f"For x = {x} and y = {y} the equation evaluates to: {result}")
        x = round((x+0.1), 2)
        if x > 100:
            x = 0
            y = round((y+0.1), 2)
        if y > 100:
            break


def maph():

  print("Enter the equation:")
  eqtn = input("(Note, you have to specify multiplication as * and division as / and ^ as exponent)\n")
  eqtn = eqtn.replace('=', '==').replace('^', '**')
  print(eqtn)
  multi2 =  eqtn.count("y")
  if multi2>0:
    return maph2(eqtn)
  else:
     pass
  x = -100

  while True:
      result = eqtn.replace('x', str(x))
      result = sympy.sympify(result)
      if result == True:
        print(f"For x = {x}, the equation is true")
        break
      x = round((x+0.1), 2)
      if x > 100:
        break

maph()