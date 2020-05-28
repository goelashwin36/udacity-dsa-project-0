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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def bangalore(call):
    return call[0][0:5] == '(080)'
def get_area_code(call):
    call_other_interloc = call[1]

    # Fixed Landline
    if call_other_interloc[:2] == '(0':
        return call_other_interloc.split(')')[0] + ')'
    # Telemarketer
    if call_other_interloc[:3] == '140':
        return call_other_interloc[:3]
    # Mobile
    else:
        return call_other_interloc[:4]

if __name__ == '__main__':
    bnglr_call = []

    for call in calls:
        if bangalore(call):
            bnglr_call.append(get_area_code(call))

    bnglr_call_resum = list(set(bnglr_call))
    bnglr_call_resum.sort()

    print("\n The numbers called by people in Bangalore have codes:")
    for call in bnglr_call_resum:
        print(call)

    bnglr_call_num = 0
    for call_prefix in bnglr_call:
        if call_prefix == "(080)":
            bnglr_call_num += 1

    print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(bnglr_call_num/len(bnglr_call)*100, 2)))
