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

if __name__ == '__main__':
    tlmk = set()
    not_tlmk = set()
    for cl, rc, st, tm in calls:
        if(cl not in not_tlmk):
            tlmk.add(cl)
        not_tlmk.add(rc)
        if(rc in tlmk):
            tlmk.remove(rc)

    for cl, rc, st in texts:
        if(cl in tlmk):
            tlmk.remove(cl)
        if(rc in tlmk):
            tlmk.remove(rc)
        not_tlmk.add(cl)
        not_tlmk.add(rc)
    tlmk = sorted(list(tlmk))
    print("These numbers could be telemarketers: ")
    print("\n".join(tlmk))
