end = 0
position = "_1"
map = ('''
1   _   4
2   _   5
3   _   6
3a  7   6a
''')
inventory = ""
notes = ""
trk = 0


def main(inventory, notes, position, map, trk, end):
    def endyy(end):
        print("You lost.")
        end += 1
        return end

    def move(position, map):
        print(map)
        ans1 = input("Which room do you want to go to?\n")
        if ans1 == "6":
            return "6"

    def rm6(inventory, notes, position, end):
        print("Dave gets the police over to arrest you.")
        end = endyy(end)
        return end
        #return endyy(end), position

    while end <= 0:       

        if position == "_1":
            position = move(position, map)
            end = main(inventory, notes, position, map, trk, end)
            return position, end
        elif position == "6":
            end = rm6(inventory, notes, position, end)
            end = main(inventory, notes, position, map, trk, end)
            return position, end
    print("Game over")
    return

main(inventory, notes, position, map, trk, end)