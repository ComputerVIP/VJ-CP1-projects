#Vincent Johnson Palindrome assignment

tst = input("What is your 'palindrome'?\n")
tst2 = tst[::-1]
if tst == tst2:
    print(f"\n{tst} is a palindrome!")
else:
    print(f"\n{tst} is not a palindrome!")