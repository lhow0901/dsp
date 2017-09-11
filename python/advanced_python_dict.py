import sys
import os
import csv

def get_dict():
    with open('faculty.csv') as f:
        faculty = csv.reader(f)
        next(faculty)
        faculty_dict = dict()
        for row in faculty:
            last_name = row[0].split(' ')[-1]
            info = row[1:4]
            if last_name not in faculty_dict:
                faculty_dict[last_name] = [info]
            else:
                faculty_dict[last_name].append(info)
        print(faculty_dict)

def get_dict2():
    with open('faculty.csv') as f:
        faculty = csv.reader(f)
        next(faculty)
        faculty_dict = dict()
        for row in faculty:
            name = tuple(row.split(' '))
            info = row[1:4]
            faculty_dict[name] = [info]
        print(faculty_dict)

get_dict2()
