#Vincent Johnson anagram
#Write a program that takes in a name and uses it to generate an anagram, the program should output at least 5 anagrams for the name that has been entered. (NOTE: They don't have to be great/ usable anagrams) 
import random

test = [input("Name?")]
test = [x for x in test]
print(test)
test2 = random.shuffle(test)
test1 = random.shuffle(test)
test0 = random.shuffle(test)
test3 = random.shuffle(test)
test4 = random.shuffle(test)
print(test2, test1, test0, test3, test4)