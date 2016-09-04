#!/usr/bin/env python 

#example of manipulig csv file  

import csv

doc=open("index.csv", "r")
doc_csv_r=csv.reader(doc)

#use for to read rows 
for(column1, column2) in doc_csv_r:
	print column1, column2
doc.close()
