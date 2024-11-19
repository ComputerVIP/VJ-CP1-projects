#Vincent Johnson Raid
count = 0
numbr = 1

def main(count, numbr):
    histo = "         "
    number = int(input("What is your number?\n"))
    if number > 9:
        print("9 or less!")
        return
    histo = histo.replace(" ", "*", number)
    print(f"{numbr}. {histo}")
    numbr += 1
    count += 1
    while count <= 4:
        main(count, numbr)
        return
    if count > 4:
        return
main(count, numbr)