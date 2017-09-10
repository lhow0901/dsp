import sys
import os
import csv

with open('faculty.csv') as f:
    faculty = csv.reader(f, skipinitialspace=True)
    next(faculty)
    degrees = list()
    for row in faculty:
        degree = row[1]
        degree = degree.replace(".","")
        degrees.append(degree)
    degrees = [i.split(' ') for i in degrees]
    all_degrees = [i for sublist in degrees for i in sublist]
    degree_count = {x:all_degrees.count(x) for x in all_degrees}
    for i in sorted(degree_count.items(), key=lambda x: x[1], reverse=True):
        print(i)
