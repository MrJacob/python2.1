#!/usr/bin/env python

#example using several basic commands in python 
#working with strings

ambient="  Cafe del Sol 2015 ";

print(ambient)

#remplacing scope of the string by another thing
ambientSun =ambient.replace("Sol",  "Mar")
print(ambientSun)

#using strip command to delete space
ambientSunOne = ambientSun.strip()

#removing space by left side using lstrip also is posible using right option with rstrip
ambientOne = ambient.lstrip()

print(ambientSunOne)
print(ambientOne)

#upper case  
print(ambientSun.upper())
print(ambient.upper().replace("2015", "2016"))
print(ambientSun,ambientSunOne)
print(ambientSun.rstrip(),ambientSunOne.lstrip())

#split string and convert in a list

ports ="8080:4848:5252:9090:6060"
print(ports)

for i in ports.split(":"):
	x=[]
	x.append(i)
        print(i)  
for z in x:
	print(z)


