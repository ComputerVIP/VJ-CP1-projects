#Vincent Johnson final project
'''
Sam-room 1
Jose-room 2
Conner-room 3-3a
Tali-room 4
Jett-room 5 MURDERER
Dave-room 6-6a

1   _   4
2   _   5
3   _   6
3a  7   6a

Room 5 only able to access first by window in 6
Room 7 can be accessed by vent in room 6a
Player needs evidence to access room 6-6a or else game ends

Room 7 locked with key in room 3a
Room 7 has lightbulb that makes you able to see in room 5
Room 7 has mop that allows you to clean up the spill hiding the map in room 3
Room 2 has the phone number in the book that allows the person to call Jett's GF in room 4, she says he hasn't been over in days
'''

position = "_1"
room_type = ""
map = ('''
1   _   4
2   _   5
3   _   6
3a  7   6a
''')
inventory = ""
notes = ""


def move(position, map, ans1):
    print(map)
    ans1 = input("Which room do you want to go to?\n")
    if ans1 == "1":
        position = "1"
    elif ans1 == "2":
        position = "2"
    elif ans1 == "3":
        position = "3"
    elif ans1 == "3a":
        print("You cannot access this from the hallway")
        move(position, map, ans1)
    elif ans1 == "4":
        position = "4"
    elif ans1 == "5":
        position = "5"
    elif ans1 == "6":
        position = "6"
    elif ans1 == "6a":
        position = "6a"
    elif ans1 == "7":
        position = "7"
    else:
        print("Not a valid room!")
        move(position, map)
def rm1(inventory, notes):
    print("The room is an apartment, there is a kitchen, bedroom and living room.")
    print("Inside the living room is a mangled body.")
    options = int(input("What would you like to do?\n1: Search body\n2: Leave\n3: Go to window"))
    if options == 1:
        print("On the body there is only an I.D. the man's name is Sam.")
        print("A note near the body says: 'You said something stupid, and now you're going to pay'")
        ans = int(input("Would you like to access your notes? 1 is yes, 2 is no"))
        if ans == 1:
            writing = input("What would you like to write?")
            notes = notes.append(writing)
        elif ans == 2:
            rm1(inventory, notes)
        else:
            print("Invalid answer")
            rm1(inventory, notes)
    elif options == 2:
        move(position, map)
    elif options == 3:
        print("You moved to room 2")
        position = "2"

def rm2(inventory, notes):
    print("The room is an apartment, there is a kitchen, bedroom and living room.")
    print("There is a notebook on the table")
    options = int(input("What would you like to do?\n1: Search notebook\n2: Leave\n3: Go to window"))
    if options == 1:
        print("In the notebook there is a number...")
        print("222-900-3648")
        ans = int(input("Would you like to access your notes? 1 is yes, 2 is no"))
        if ans == 1:
            writing = input("What would you like to write?")
            notes = notes.append(writing)
        elif ans == 2:
            rm2(inventory, notes)
        else:
            print("Invalid answer")
            rm2(inventory, notes)
    elif options == 2:
        move(position, map)
    elif options == 3:
        print("You can move to room 3 or 1")
        ans = int(input("1 for room 1, 2 for room 3"))
        if ans == 1:
            position == "1"
        elif ans == 2:
            position == "2"
        else:
            print("Invalid answer")
            rm2(inventory, notes)


#Working on this part, key in room 3a
def rm3(inventory, notes):
    print("The room is an apartment, there is a kitchen, bedroom and living room.")
    print("There is a spill on the floor, and an open doorway")
    options = int(input("What would you like to do?\n1: Go to the spill\n2: Leave\n3: Go through the door"))
    if options == 1:
        print("The spill is stained")
        if "Mop" in inventory:
            print("There is a map under the spill, it shows a path from room 5 to room 1 and room 3 to room 5")
    elif options == 2:
        move(position, map)
    elif options == 3:
            position == "3a"
def rooms(position):
    if position == "1":
        rm1(inventory, notes)
    if position == "2":
        rm2(inventory, notes)