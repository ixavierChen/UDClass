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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
firstIncomingNumber = texts[0][0]
firstAnsweringNumber = texts[0][1]
firstTime = texts[0][2]
print(f"First record of texts, {firstIncomingNumber} texts {firstAnsweringNumber} at time {firstTime}")
lastIncomingNumber = calls[-1][0]
lastAnsweringNumber = calls[-1][1]
lastTime = calls[-1][2]
lastDuring = calls[-1][3]
print(f"First record of texts, {lastIncomingNumber} texts {lastAnsweringNumber} at time {lastTime} ,lasting {lastDuring} seconds")

