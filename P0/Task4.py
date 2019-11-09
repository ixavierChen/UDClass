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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
import allcall

allcallSet  = allcall.getAllCallSet()

try:
    for recode in calls:
        allcallSet.remove(recode[1])
    for textcode in texts:
        allcallSet.remove(textcode[0])
        allcallSet.remove(textcode[1])
except KeyError as identifier:
    pass

telmarklist = list(allcallSet)
telmarklist.sort()
print(f"These numbers could be telemarketers: ")
for telemark in telmarklist:
    print(telemark)
    