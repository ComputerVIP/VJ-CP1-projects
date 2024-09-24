#Vincent Johnson Pig Latin Converter
#Write a function that will take in any word and convert it into pig latin
x = 0
var3 = 0
var = input("What is the word you want to convert?\n")
var1 = [i for i in var]
leng = len(var1)
var2 = str(var1[0][0])
var2 = var2.lower()
def end():
    var4 = var3 + var2
    print(f"\n{var1}\n{leng}\n {var4}")
while True:
    x +=1
    var3 = var1[x][0]
    if x < leng:
        end()