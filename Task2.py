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

if __name__ == '__main__':
    maxTime = -1
    callDurations = dict()
    record = ""
    for cl, rc, ts, t in calls:
        t = int(t)
        if(cl in callDurations):
            callDurations[cl] += t
        else:
            callDurations[cl] = t
        if(rc in callDurations):
            callDurations[rc] += t
        else:
            callDurations[rc] = t
        if(callDurations[cl] > maxTime):
            maxTime = callDurations[cl]
            record = cl
        if(callDurations[cl] > maxTime):
            maxTime = callDurations[cl]
            record = rc

    print("{} spent the longest time, {}, seconds, on the phone during September 2016.".format(record,maxTime))
