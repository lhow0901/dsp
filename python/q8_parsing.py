# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

#Reads the football.csv file and stores data as a list of lists (without headers).
teamslist = list()
with open('football.csv', 'r') as f:
    reader = csv.reader(f)
    teamslist = list(reader)
teamslist.pop(0)

#Iterates through the list of stats by football team and stores the value of each
#teams' goals 'for' minus their goals 'against' in a new list. Sets the value of
#an index variable i to the index of the lowest value of the new list.
dif_list = list()
for t in teamslist:
    dif_list.append(int(t[5]) - int(t[6]))
i = dif_list.index(min(dif_list))

print(teamslist[i][0])
