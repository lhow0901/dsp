import sys
import os
from datetime import datetime

def difference_in_days(date1, date2):
    date1 = datetime.strptime(date1, "%m-%d-%Y")
    date2 = datetime.strptime(date2, "%m-%d-%Y")
    difference = date2 - date1
    return(difference.days)

start_date = sys.stdin.readline().strip()
stop_date = sys.stdin.readline().strip()
print(difference_in_days(start_date,stop_date))
