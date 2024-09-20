import re

def maph2(eqtn):
    print("Running maph2")
    import sympy

    x = -100
    y = -100
    while True:
        try:
            result = sympy.sympify(eqtn.replace('x', str(x)).replace('y', str(y)))
            eqtn2 = eqtn.replace('x', str(x)).replace('y', str(y)).replace('==', ' = ')
            if result is True:
                print(f"For x = {x} and y = {y} the equation [\ {eqtn2} /] evaluates to: {result}")
            x = round((x+0.1), 2)
            if x == 100:
                x = -100
                y = round((y+0.1), 2)
            if y == 100:
                break
        except:
            print("\n//\n\nError occurred...")
            break


def maph():
  import sympy

  print("Enter the equation:")
  eqtn = input("(Note, you have to specify multiplication as * and division as /)\n")
  eqtn = eqtn.replace('=', '==')
  print(eqtn)
  multi2 =  eqtn.count("y")
  if multi2>0:
    return maph2(eqtn)
  x = -100

  while True:
    try:
      #eqtn=re.sub("\(.*?\)","()",eqtn)
      eqtn2 = eqtn.replace('x', str(x)).replace('==', ' = ')
      result = sympy.sympify(eqtn.replace('x', str(x)))
      print(eqtn2)
      if result is True:
        print(f"For x = {x}, the equation is true")
      x = round((x+0.1), 2)
      if x == 101:
        break
    except:
      break

maph()