#Read age data from a CSV file and calculate the average of the age column
#Author: Carmine Giardino

import csv
FILENAME= "data.csv"
DATADIR = "data/"


with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # skipping header
            pass
        else: # processing data lines
            total += line[1] # taking second column "age"
        linecount += 1
    print (f"The average is {total/(linecount-1)}") # minus 1 for header