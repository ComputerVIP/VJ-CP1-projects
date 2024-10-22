#Vincent Johnson Password Validator
pas = ""
char = False
cnt = False
num = False
count2 = int(0)

def main(pas, char, cnt, num, count2):
    pas = input("What is your password? (Has to have 8 characters, one has to be a number, and another has to be a special character, @, #, $, %, &, +, =)\n")
    if pas.count("@") >= 1:
        char = True
    if pas.count("#") >= 1:
        char = True
    if pas.count("$") >=1:
        char = True
    if pas.count("%") >= 1:
        char = True
    if pas.count("&") >= 1:
        char = True
    if pas.count("+") >= 1:
        char = True
    if pas.count("=") >= 1:
        char = True

    if len(pas) >= 8:
        cnt = True

    while count2 != 10:
        if pas.count(str(count2)) >= 1:
            num = True
            count2 += 1
        else:
            count2 += 1

    if count2 >=10:
        while cnt != True:
            print("Password does not contain enough characters! (Must be 8)")
            main(pas, char, cnt, num, count2)
            return
        while char != True:
            print("Does not have a special character!")
            main(pas, char, cnt, num, count2)
            return
        while num != True:
            print("Password does not contain a number!")
            main(pas, char, cnt, num, count2)
            return
        else:
            print("You have a good password!")
            return
main(pas, char, cnt, num, count2)