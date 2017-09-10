import sys
import os

def write_to_csv(list_of_emails):
    list_of_emails = list(['bellamys@mail.med.upenn.edu', 'warren@upenn.edu', 'bryanma@upenn.edu'])
    with open('emails.csv','w') as f:
        f.write('email\n')
        for email in list_of_emails:
            f.write(email+"\n")
