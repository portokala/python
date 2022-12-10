import csv
from cs50 import get_string

file = open("adname.csv", "w+", newline='')

name = get_string("Name: ")
number = get_string ("Number: ")

writer = csv.writer(file)
writer.writerow((name, number))
