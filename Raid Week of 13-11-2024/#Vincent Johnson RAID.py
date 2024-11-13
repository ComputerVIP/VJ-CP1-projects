#Vincent Johnson RAID

import time
def main():
    tme = int(input("How long do you want a timer for?\n"))
    while tme > 0:
        time.sleep(1)
        tme -= 1
        print(f"You have {tme} second(s) left in the timer!")
    if tme <= 0:
        print("Timer over!\n\n\n")
        ans = int(input("Do you want to run again? 1 = y   2 = n\n"))
        if ans == 1:
            main()
            return
        else:
            print("Have a nice day!")
            return
main()