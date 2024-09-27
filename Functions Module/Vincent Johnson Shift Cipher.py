#Create a program with a function that that takes in a users string and uses a shift cypher to turn the string into a secret code. 

#BONUS: 

#Write another function that decodes someone else's secret message. 

#Will decode if you use negative numbers :)
shift = int(input("How many do you want to shift by?\n"))
def shifttext(shift):
    inpt = input('Input text:\n')
    data = list(inpt)
    for i, char in enumerate(data):
        if char.isalpha():
            data[i] = chr((ord(char) + shift - ord('a')) % 26 + ord('a')) 
            print(data)
        else:
            data[i] = char
    output = ''.join(data)
    print(output)
    return
shifttext(shift)