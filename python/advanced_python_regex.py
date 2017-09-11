import sys
import os
import csv

def count_degrees(csv_file_name):
    with open(csv_file_name) as f:
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
        print(degree_count)

def count_titles(csv_file_name):
    with open(csv_file_name) as f:
        faculty = csv.reader(f, skipinitialspace=True)
        next(faculty)
        titles = list()
        for row in faculty:
            title = row[2]
            title = title.replace(" is "," of ")
            titles.append(title)
        title_count = {x:titles.count(x) for x in titles}
        print(title_count)

def emails(csv_file_name):
    with open(csv_file_name) as f:
        faculty = csv.reader(f)
        next(faculty)
        emails = list()
        for row in faculty:
            email = row[3]
            emails.append(email)
        for email in sorted(emails):
            print(email)

def unique_domains(emails):
    domains = list()
    for email in emails:
        email = email.split("@")[1]
        domains.append(email)
    domains = sorted(set(domains))
    print(domains)
