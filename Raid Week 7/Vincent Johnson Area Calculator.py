#Vincent Johnson Week 7 Raid

#Asks if has keyboard, making program look nicer ;)
print("\n /////This function uses the keyboard module, you must run 'pip install keyboard' to continue///// \n")
ans = input("Did you install keyboard? y/n\n")

#This variable acts as a timer, if it reaches a certain value it will stop
tmr = 0

#Square
def sqr():
    data = int(input("What is the length?"))
    ad = data * data
    print(f"The area of your square is {ad}")

#Rectangle
def rect():
    data = int(input("What is the length?"))
    data2 = int(input("What is the width?"))
    ad = data * data2
    print(f"The area of your rectangle is {ad}")
    
#Triangle
def tri():
    data = int(input("What is the length?"))
    data2 = int(input("What is the height?"))
    ad = data * data2
    ad = ad/2
    print(f"The area of your triangle is {ad}")

#Circle DIAMETRE
def crcd():
    data = int(input("What is the diameter?"))
    ad = data/2
    ad = ad**2
    ad = ad*3.1415926535897932384626
    print(f"The area of your circle is {ad}")

#Circle RADIUS
def crcr():
    data = int(input("What is the radius?"))
    ad = (data**2)*3.1415926535897932384626
    print(f"The area of your circle is {ad}")

#Circle MENU
def crc(tmr):
    print("For diametre, press 1\nFor radius, press 2")
    while True:
        tmr += 1
        if keyboard.is_pressed("1"):
            tmr = 0
            crcd()
            break
        if keyboard.is_pressed("2"):
            tmr = 0
            crcr()
            break
        if tmr > 50000:
            print("\n\nWaited too long, exiting...")
            break


#Trapezoid
def trap():
    data = int(input("What is the length of the bottom?"))
    data2 = int(input("What is the length of the top?"))
    data3 = int(input("What is the hight?"))
    ad = data + data2
    ad = ad / 2
    ad = ad * data3
    print(f"The area of your triangle is {ad}")

#Main menu
if ans == "y":
    import keyboard
    print("For rectangle, press 1\nFor square, press 2\nFor triangle, press 3\nFor circle, press 4\nFor trapezoid, press 5\n")
    while True:
        tmr = 0
        tmr += 1
        if keyboard.is_pressed("1"):
            tmr = 0
            sqr()
            break
        if keyboard.is_pressed("2"):
            tmr = 0
            rect()
            break
        if keyboard.is_pressed("3"):
            tmr = 0
            tri()
            break
        if keyboard.is_pressed("4"):
            tmr = 0
            crc(tmr)
            break
        if keyboard.is_pressed("5"):
            tmr = 0
            trap()
            break

        if tmr > 50000:
            print("\n\nWaited too long, exiting...")
            break