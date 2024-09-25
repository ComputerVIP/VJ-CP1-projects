#Create a program with a function that that takes in a users string and uses a shift cypher to turn the string into a secret code. 

#BONUS: 

#Write another function that decodes someone else's secret message. 

def code():
    var = input("What do you want to encode?")
    var1 = [i for i in var]
    leng = int(len(var))
    leng2 = round(leng/2)
    var2 = str(var1[0:leng2])
    var3 = str(var1[leng2:leng])
    var4 = var3 + var2

    print(leng2, var2, var3, leng, var4)
code()