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
months = dict()
months["01"] = "January"
months["02"] = "February"
months["03"] = "March"
months["04"] = "April"
months["05"] = "May"
months["06"] = "June"
months["07"] = "July"
months["08"] = "August"
months["09"] = "September"
months["10"] = "October"
months["11"] = "November"
months["12"] = "December"

if __name__ == '__main__':
    maxTime = -1
    record = []
    for rec in calls:
        if(int(rec[3]) > maxTime):
            maxTime = int(rec[3])
            record = rec

    print("{} spent the longest time, {}, seconds, on the phone during {} {}.".format(record[0],record[3], months[record[2][3:5]], record[2][6:10]))
