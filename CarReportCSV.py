#!/usr/bin/env python 
__script_created_by__ = "Jacob Ordonez"

#example write in csv file 

#import modules
import csv 

doc=open("GrupCarReport.csv", "w")

doc_csv_w=csv.writer(doc)

#nest list to entry values 

list =[["Toyota", 2016, "Mecanic"],["Bugatti", 2012, "Mecanic"],["BMW", 2016, "Automatic"],["Ferrari", 2010, "Mecanic"],["Honda", 2014, "Automoatic"],
      ["Bugatti", 2015, "Mecanic"]]

#for to write in csv file 

for car_entry in list:
	doc_csv_w.writerow(car_entry)

doc.close()



