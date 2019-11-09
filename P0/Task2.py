"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import allcall
timeDict = {}.fromkeys(allcall.getAllCallSet(),0)

longestCall = calls[0][0]
longestTime = int(calls[0][3])
for call in calls:
    callnumber = call[0]
    answernumber = call[1]
    if timeDict[callnumber] == 0:
        timeDict[callnumber] = int(call[3])
    else:
        timeDict[callnumber] += int(call[3])
    if timeDict[callnumber] > longestTime:
        longestTime = timeDict[callnumber]
        longestCall = callnumber
    if timeDict[answernumber] == 0:
        timeDict[answernumber] = int(call[3])
    else:
        timeDict[answernumber] += int(call[3])
    if timeDict[answernumber] > longestTime:
        longestTime = timeDict[answernumber]
        longestCall = answernumber

print(f"{longestCall}spent the longest time, {longestTime} seconds, on the phone during September 2016.")



    
