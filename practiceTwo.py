#!/usr/bin/env python 

#working with lists 

numbers=[9,8,2,5,10,15,12,19,7,1,12,17,3,20,6,2]

print(numbers)

#order list by print, do not modify the original array 
print("Sort List: ")
print(sorted(numbers))

numbers[2]=14;
#order list by print, do not modify the origianl array
print(sorted(numbers, reverse=True))


#permaneng change in list

stages=["SPRING", "FALL", "SUMMER", "WINTER"]

#sort values 
stages.sort()

for  st in range(len(stages)):
	print(stages[st].lower())



#example of sets 

net_Primary=set("190.144.90.10,199.144.90.20,190.144.90.40,199.144.90.50,sun")
net_Secundary=("u","190.144.12.60","190.144.12.50","190.144.90.40","190.144.12.90","sun")
print(net_Primary)
print(net_Secundary)

print(net_Primary.intersection(net_Secundary))

