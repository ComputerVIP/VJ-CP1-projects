#Vincent Johnson Proficiency test Conditionals Module

name = input("What is your username?\n")
name = name.lower()
admin = ["admin","dev","pedro","ethan","gabe","sam","mr m","jimothy"]
users = ["nerd","void","empty","pain","anguish","darkness","sad","anger"]
if name in admin:
    print("Hello admin.")
elif name in users:
    print("Hello user.")
else:
    print("You are not an admin or a user.")