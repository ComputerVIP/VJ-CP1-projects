#Vincent Johnson Shopping List Manager
spl = []

def add(spl):
    ad = input("What do you want to add?")
    spl = spl.append(ad)
    print("Here is your new list:\n",spl)

def dele(spl):
    print(spl)
    ad = input("What do you want to delete?")
    spl = spl.remove(ad)
    print("Here is your new list:\n",spl)

def main():
    ans = int(input("Press 1 for add items\nPress 2 to remove items\n"))
    if ans == 1:
        add(spl)
        return
    if ans == 2:
        dele(spl)
        return
    else:
        print("Not 1 or 2\n")
        return
main()