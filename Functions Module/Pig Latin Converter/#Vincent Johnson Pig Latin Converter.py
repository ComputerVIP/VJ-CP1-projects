#Vincent Johnson Pig Latin Converter
#Write a function that will take in any word and convert it into pig latin
x = 0
var0 = ""
var3 = ""
var = input("What is the word you want to convert?\n")
var1 = [i for i in var]
leng = str(len(var1))
leng2 = int(leng)
var2 = str(var1[0][0])
var2 = var2.lower()
vowels = 'a', 'e', 'i', 'o', 'u' or x == 'A' or 
        x == 'E' or x == 'I' or x == 'O' or 
        x == 'U'"

def find_first_vowel(var):
    i = 0   
    while i < len(var):
        if var[i] in vowels:
            return i
        i += 1
    return -1

def end():
    var4 = var3 + var2
    var4 = var4 + "ay"
    var4 = var4.capitalize()
    print(f"{var4}")
while True:
    x +=1
    xy = int(x)
    var0 = var1[xy][0]
    var3 = var3 + var0
    if x >= (leng2-1):
        end()
        break