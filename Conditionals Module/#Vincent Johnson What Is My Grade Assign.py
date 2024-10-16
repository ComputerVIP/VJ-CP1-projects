#Vincent Johnson What Is My Grade Assignment

'''
A 1200 - 1128 Points
A- 1127 - 1080 Points
B+ 1079 - 1044 Points
B+ 1043 - 1008 Points
B- 1007 - 960 Points
C+ 959 - 924 Points
C 923 - 888 Points
C- 887 - 840 Points
D+ 839 - 804 Points
D 803 - 768 Points
D- 767 - 720 Points
F 719 - 0 Points
'''
def main():
    grade = float(input("What is your grade percentage?\n"))
    if (grade >94.0) is True:
        print("You have an A!")
    elif (94.0>grade>90.0) is True:
        print("You have an A-!")
    elif (90.0>grade>87.0) is True:
        print("You have a B+!")
    elif (87.0>grade>84.0) is True:
        print("You have a B!")
    elif (84.0>grade>80.0) is True:
        print("You have a B-!")
    elif (80.0>grade>77.0) is True:
        print("You have a C+!")
    elif (77.0>grade>74.0) is True:
        print("You have a C!")
    elif (74.0>grade>70.0) is True:
        print("You have a C-!")
main()