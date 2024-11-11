'''
GOAL:
Build a program that allows a user to create a character

INSTRUCTIONS:
Let user select a class, and a race (you should also have them select a character name). Base on the user choices print out their character stats:

-health

-strength

-dexterity

-intelligence
'''
#Vincent Johnson

hp = 0
sgth = 0
dex = 0
inte = 0

race = int(input("What race would you like?\n1. Orc\n2. Elf\n3. Human\n4. Dwarf\n5. Alien\n"))
if race < 1:
    print("You can't do that :(")
if race > 5:
    print("YOU CAN'T DO THAT! :<")
if race == 1:
    hp += 10
    sgth += 11
    dex += -2
    inte += -4
    my_race = "Orc"
if race == 2:
    hp += 7
    sgth += 4
    dex += 10
    inte += 9
    my_race = "Elf"
if race == 3:
    hp += -1
    sgth += -1
    dex += 3
    inte += -2
    my_race = "Human"
if race == 4:
    hp += 3
    sgth += 13
    dex += -3
    inte += 3
    my_race = "Dwarf"
if race == 5:
    hp += 2
    sgth += 3
    dex += 10
    inte += 15
    my_race = "Alien"
race2 = int(input("What class would you like??\n1. Warrior\n2. Bard\n3. Medic\n"))
if race2 < 1:
    print("You can't do that :(")
if race2 > 3:
    print("YOU CAN'T DO THAT! :<")
if race2 == 1:
    hp += 7
    sgth += 4
    dex += 2
    inte += -2
    my_class = "Warrior"
if race2 == 2:
    hp += 20
    sgth += -20
    dex += -20
    inte += -5
    my_class = "Bard"
if race2 == 3:
    hp += -6
    sgth += -1
    dex += 5
    inte += 7
    my_class = "Medic"
print(f"\n\nThese are your stats:\nClass: {my_class}\nRace: {my_race}\n\n/////////////\nHealth: {hp}\nStrength: {sgth}\nDexterity: {dex}\nIntelligence: {inte}")