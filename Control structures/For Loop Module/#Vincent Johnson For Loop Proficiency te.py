#Vincent Johnson For Loop Proficiency test
def maf():
    number = int(input("What number do you want the multiplication table for?\n"))
    state = 1
    if number > 12:
        print("Hey, less than 12!")
        maf()
        return
    if number < 1:
        print("Hey! At lest 1!")
        maf()
        return
    while state <= 12:
        number2 = number * state
        print(f"{number} x {state} = {number2}")
        state +=1
    if state > 12:
        print(f"That is the multiplication table for {number}\n")
        return
maf()