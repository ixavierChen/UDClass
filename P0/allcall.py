"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def getAllCallSet():
    calls.extend(texts)
    count_set = set()
    for callInfo in calls:
        count_set.add(callInfo[0])
        count_set.add(callInfo[1])

    return count_set
