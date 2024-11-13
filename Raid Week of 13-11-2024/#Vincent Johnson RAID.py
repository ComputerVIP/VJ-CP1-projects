#Vincent Johnson RAID

import time
def main():
    tme = int(input("How long do you want a timer for?\n"))
    tim = 0
    while tim < tme:
        time.sleep(1)
        tim += 1
        print(f"You are at {tim} second(s)!")
    if tim >= tme:
        print("Timer over!\n\n\n")
        ans = int(input("Do you want to run again? 1 = y   2 = n\n"))
        if ans == 1:
            main()
            return
        else:
            print("Have a nice day!")
            return
main()