#Vincent Johnson Proficiency test Conditionals Module

name = input("What is your username?\n")
name = name.lower()
admin = ["admin","dev","pedro","ethan","gabe"]
if name in admin:
    print("Hello admin.")
else:
    print("You are not an admin.")