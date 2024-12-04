#Vincent Johnson FINAL
'''
Game Layout and Key Information:

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
Player needs evidence to access room 6 or else game ends

Room 7 locked with key in room 3a
Room 7 has lightbulb that makes you able to see in room 5
Room 7 has mop that allows you to clean up the spill hiding the map in room 3
Room 2 has the phone number in the book that allows the person to call Jett's GF in room 4, she says he hasn't been over in days
'''

position = "_1"  # Player starts in the hallway
map = ('''
1   _   4
2   _   5
3   _   6
3a  7   6a
''')
inventory = []
notes = ""
trk = 0

def main(inventory, notes, position, map, trk):
    def move(position, map):
        print(map)
        ans1 = input("Which room do you want to go to?\n")
        if ans1 == "1":
            return "1"
        elif ans1 == "2":
            return "2"
        elif ans1 == "3":
            return "3"
        elif ans1 == "3a":
            print("You cannot access this from the hallway.")
            return move(position, map)
        elif ans1 == "4":
            return "4"
        elif ans1 == "5":
            return "5"
        elif ans1 == "6":
            return "6"
        elif ans1 == "6a":
            print("You cannot access this from the hallway.")
            return move(position, map)
        elif ans1 == "7":
            return "7"
        else:
            print("Not a valid room!")
            return move(position, map)

    def rm1(inventory, notes, position):
        print("The room is an apartment, there is a kitchen, bedroom and living room.")
        print("Inside the living room is a mangled body.")
        options = int(input("What would you like to do?\n1: Search body\n2: Leave\n3: Go to window\n"))
        if options == 1:
            print("On the body there is only an I.D. the man's name is Sam. It looks like he was hit over the head, a rubber handle of something sits nearby.")
            print("A note near the body says: 'You said something stupid, and now you're going to pay'.")

            ans = int(input("Would you like to access your notes? 1 is yes, 2 is no.\n"))
            if ans == 1:
                writing = input("What would you like to write?\n")
                notes = notes + writing
                print(f"\nNotes:\n{notes}\n")
                rm1(inventory, notes, position)
            elif ans == 2:
                rm1(inventory, notes, position)
        elif options == 2:
            position = "_1"
            return position
        elif options == 3:
            print("You moved to room 2")
            position = "2"
            return position
        else:
            print("Not a valid answer!")
            return rm1(inventory, notes, position)

    def rm2(inventory, notes, position):
        print("The room is an apartment, there is a kitchen, bedroom and living room.")
        print("There is a notebook on the table")
        options = int(input("What would you like to do?\n1: Search notebook\n2: Leave\n3: Go to window\n"))

        if options == 1:
            print("In the notebook there is a number...")
            print("222-900-3648")

            ans = int(input("Would you like to access your notes? 1 is yes, 2 is no.\n"))
            if ans == 1:
                writing = input("What would you like to write?\n")
                notes = notes + writing
                print(f"\nNotes:\n{notes}\n")
                rm2(inventory, notes, position)
            elif ans == 2:
                rm2(inventory, notes, position)
        elif options == 2:
            position = "_1"
            return position
        elif options == 3:
            print("You can move to room 3 or 1")
            ans = int(input("Enter 1 for room 1, enter 2 for room 3.\n"))
            if ans == 1:
                position = "1"
                return position
            elif ans == 2:
                position = "3"
                return position
        else:
            print("Not a valid answer!")
            return rm2(inventory, notes, position)

    def rm3(inventory, notes, position):
        print("The room is an apartment, there is a kitchen, bedroom and living room.")
        print("There is a spill on the floor, and an open doorway.")
        options = int(input("What would you like to do?\n1: Go to the spill\n2: Leave\n3: Go through the door\n"))
        if options == 1:
            print("The spill is stained, but there is something under it.")
            if "Mop" in inventory:
                print("There is a map under the spill, it shows a path from room 5 to room 1 and room 3 to room 5.")
                inventory = inventory + "Map"
                ans = int(input("Would you like to access your notes? 1 is yes, 2 is no.\n"))
            if ans == 1:
                writing = input("What would you like to write?\n")
                notes = notes + writing
                print(f"\nNotes:\n{notes}\n")
                rm3(inventory, notes, position)
            elif ans == 2:
                rm3(inventory, notes, position)
        elif options == 2:
            position = "_1"
            return position
        elif options == 3:
            position = "3a"
            return position
        else:
            print("Not a valid answer!")
            return rm3(inventory, notes, position)

    def rm3a(inventory, notes, position):
        print("This room just has a table and a letter on the table.")
        options = int(input("What would you like to do?\n1: Open the letter\n2: Leave\n"))
        if options == 1:
            if "Key" not in inventory:
                print("The letter has a key inside it.")
                inventory.append("Key")
                print("\nKey has been added to your inventory\n")
                rm3a(inventory, notes, position)
            else:
                print("You have already grabbed the key.")
                rm3a(inventory, notes, position)
        elif options == 2:
            position = "3"
            return position
        else:
            print("Not a valid answer!")
            return rm3a(inventory, notes, position)

    def rm4(inventory, notes, trk, position):
        print("The room is an apartment, there is a kitchen, bedroom and living room.")
        print("There is a phone on the table.")
        options = int(input("What would you like to do?\n1: Go to the phone\n2: Leave\n3: Go through the door\n"))
        if options == 1:
            print("You head up to the phone")
            phone_num = input("What phone number do you want to dial? (include dashes and no spaces in the phone number)\n")
            if phone_num == "222-900-3648":
                if trk == 0:
                    print("DIALING...")
                    print("???: Hello?")
                    print("???: Is this Jett?")
                    print("???: Oh honey, I've missed you! You haven't stopped by in 3 days!")
                    print("???: Conner was over grabbing some tools yesterday, but you weren't there!")
                    print("???: Oh is this not Jett?")
                    print("???: ...")
                    print("???: Well tell him that Graciepoo misses him.")
                    print("Grace: Goodbye.")
                    inventory = inventory + "Phone"
                    trk += 1
                    ans = int(input("Would you like to access your notes? 1 is yes, 2 is no.\n"))
                    if ans == 1:
                        writing = input("What would you like to write?\n")
                        notes = notes + writing
                        print(f"\nNotes:\n{notes}\n")
                        rm4(inventory, notes, trk, position)
                    elif ans == 2:
                        rm4(inventory, notes, trk, position)
        elif options == 2:
            position = "_1"
            return position
        else:
            print("Not a valid answer!")
            return rm4(inventory, notes, trk, position)

    def rm5(inventory, notes, position):
        print("The room is too dark to see anything")
        if "Lightbulb" in inventory:
            print("You put the lightbulb in the fixture, you see a pile of tools in the apartment, the window is locked.")
            inventory = inventory + "Tools"
            ans = int(input("Would you like to access your notes? 1 is yes, 2 is no\n"))
            if ans == 1:
                writing = input("What would you like to write?\n")
                notes = notes + writing
                print(f"\nNotes:\n{notes}\n")
                pass
            elif ans == 2:
                pass
        options = int(input("What would you like to do?\n1: Leave"))
        if options == 1:
            position = "_1"
            return position
        else:
            print("Not a valid answer!")
            return rm5(inventory, notes, position)

    def rm6(inventory, notes, position):
        print("As you enter the room a man confronts you.")
        print("'I told you not to come back until you had something to prove me innocent.'") #Logic for inventory
        options = int(input("What would you like to do?\n1: Search window\n2: Leave\n"))
        if options == 1:
            print("You see a window leading into room 5")
            return position
        elif options == 2:
            position = "_1"
            return position

    def rm6a(inventory, notes, position):
        print("This room has a door leading outside and a vent.")
        options = int(input("What would you like to do?\n1: Enter vent\n2: Go through the door\n"))
        if options == 1:
            position = "7"
            return position
        elif options == 2:
            position = "6"
            return position

    def rm7(inventory, notes, position):
        print("This room is a janitorial closet. There is a mop, lightbulb, boxes, vent, and window.")
        options = int(input("What would you like to do?\n1: Take mop\n2: Leave\n3. Take lightbulb\n4. Enter vent\n5. Go to window")) #Window to room 3a
        if options == 1:
            inventory = inventory + "Mop"
            print("\nMop has been added to your inventory\n")
            return position
        elif options == 2:
            position = "_1"
            return position
        elif options == 3:
            inventory = inventory + "Lightbulb"
            print("\nLightbulb has been added to your inventory\n")
            return position
        elif options == 4:
            position = "6a"
            return position
        
    if position == "_1":
        position = move(position, map)
        main(inventory, notes, position, map, trk)
    elif position == "1":
        position = rm1(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "2":
        position = rm2(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "3":
        position = rm3(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "3a":
        position = rm3a(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "4":
        position = rm4(inventory, notes, trk, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "5":
        position = rm5(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "6":
        position = rm6(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "6a":
        position = rm6a(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)
    elif position == "7":
        position = rm7(inventory, notes, position)
        if position == "_1":
            main(inventory, notes, position, map, trk)

main(inventory, notes, position, map, trk)