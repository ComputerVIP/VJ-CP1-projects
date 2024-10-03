#Vincent Johnson Shopping List Manager
spl = []
ans1 = ""

def add(spl, ans1):
    ad = input("What do you want to add?\n")
    ad = ad.lower()
    ad = ad.replace(" ", ", ")
    spl.append(ad)
    ad = ""
    print("\nHere is your new shopping list:\n",spl)
    ans1 = int(input("Press 1 for again\nPress 2 for deletion\nPress 3 for end\n"))
    if ans1 == 1:
        ans1 = 0
        add(spl, ans1)
        return
    if ans1 == 2:
        ans1 = 0
        dele(spl, ans1)
        return
    else:
        print("Goodbye...\n")
        return

def dele(spl, ans1):
    print(spl)
    ad = input("What do you want to delete?\n")
    ad = ad.lower()
    spl.remove(ad)
    ad = ""
    print("Here is your new shopping list:\n",spl)
    ans1 = int(input("Press 1 for again\nPress 2 for addition\nPress 3 for end\n"))
    if ans1 == 1:
        ans1 = 0
        dele(spl, ans1)
        return
    if ans1 == 2:
        ans1 = 0
        add(spl, ans1)
        return
    else:
        print("Goodbye...\n")
        return

def main():
    ans = int(input("Press 1 for add items\nPress 2 to remove items\nPress 3 to end\n"))
    if ans == 1:
        add(spl, ans1)
        return
    if ans == 2:
        dele(spl, ans1)
        return
    else:
        print("Goodbye...\n")
        return
main()