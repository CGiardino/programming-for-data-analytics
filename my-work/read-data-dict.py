#Read age data from a CSV file and calculate the average of the age column using dict reader
#Author: Carmine Giardino

import csv
FILENAME= "data.csv"
DATADIR = "data/"

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
        count +=1
print (f"average is {total / count}") # no header to skip as it is managed by DictReader