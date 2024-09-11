#Vincent Johnson
#INSTRUCTIONS:
#Create a program that calculates the number of tables needed for a school awards ceremony. Make sure you are using variables to create your equation, and that you are resetting the variables instead of changing the original numbers. 

#DATA:
#Faculty and Staff attending: 32

#Students being awarded: 100

#Each student is allowed 2 guests

#Each table seats 12 people

#CHANGES:
#1 student cannot attend, adjust to not count them or their guests. 

#3 teachers cannot attended 

#15 students only have 1 guest coming

#1 members of the school board are going to attend

#Initial extimate:

fac = 32
std = 100
gst = 2
tbl = 12

#Revised estimate

fac = 30
#Students split into two groups, one with 2 people coming, one with only one person coming, the plus one is representing the student recieving the award
std = 84
gst = 2+1
std2 = 15
gst2 = 1+1
tbl = 12

ttl = fac+(std*gst)+(std*gst2)
print(ttl)
print(round(ttl/tbl))