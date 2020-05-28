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

if __name__ == '__main__':

    firstText = texts[0]
    print("First record of texts, {} texts {} at time {}".format(firstText[0], firstText[1], firstText[2]))

    firstCall = calls[0]
    print("First record of calls, {} calls {} at time {}".format(firstCall[0], firstCall[1], firstCall[2]))
