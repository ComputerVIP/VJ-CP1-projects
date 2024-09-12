#Vincent Johnson

# INSTRUCTIONS:
#Write a program with 2 variables, one that has a user input asking for the temperature in Celsius. The other variable using the temperature given to convert that temperature to Fahrenheit (Yes I want you to store that in a variable). 

#Then create a print statement that outputs both the temperature in Celsius and Fahrenheit. 

#Example:

#Enter temperature in Celsius: 20

#When it is 20 degrees Celsius it is 68 degrees Fahrenheit

#EQUATION:
#(Celsius * 9/5)+32

cel = int(input("What's the temperature in celcuis?\n"))
far = (cel * 9/5)+32
print(f"The temperature in Celcuis is {cel} and the temperature in farenheight is {far}.")