# Problem statement in description

import datetime

cur_date = datetime.datetime.now()

print("Current Date:", cur_date)
print("Year:", cur_date.year)
print("Weekday_Long:", cur_date.strftime("%A"))
print("Weekday_Short:", cur_date.strftime("%a"))

'''

Output:

Current Date: 2020-10-11 18:44:37.305602
Year: 2020
Weekday_Long: Sunday
Weekday_Short: Sun

'''
