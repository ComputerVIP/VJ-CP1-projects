#Vincent Johnson Formatting Proficiency Test
var = int(input("Enter a number:\n"))
txt1 = "Your number with commas is: {:,}"
txt2 = "Your number with 4 decimal places is {:.4f}"
txt3 = "Your number as a percentage is: {:%}"
txt4 = "Your number as money is ${:.2f}"
print(txt1.format(var))
print(txt2.format(var))
print(txt3.format(var))
print(txt4.format(var))