#!/usr/bin/env python 

__file_created_by="Jacob Ordonez"

#import modules 
import csv

doc=open("GrupCarReport.csv", "r")
doc_csv=csv.reader(doc)

#for to read each row of the file 

for (fieldOne,fieldTwo,fieldThree) in doc_csv:
	print fieldOne, fieldTwo, fieldThree
  

