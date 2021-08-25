
#prompt user to input name
name = input('Your name is: ')

#make sure name with at least 1 character has been entered
while len(name) == 0:
    print('Please enter at least one character.')
    name = input('Your name is: ')

#prompt user to input birth month
month = input('Your birth month is: ')

#make sure they enter something for birth month
while len(month) == 0:
    print('Please enter at least one character.')
    month = input('Your birth month is: ')



#print name
print(f'Hello, {name}!')

#check if month is august or August and print happy birthday month if true
#I commented this out in favor of the 'compare to current month' method below!
#if month == 'August' or month == 'august':
#    print('Happy birthday month!')

#print number of letters in name
print(f'There are {len(name)} letters in your name.')



#next 3 lines found here: https://www.geeksforgeeks.org/get-current-date-using-python/
from datetime import date 
today = date.today() #get the current date
current_month_number = today.month #get just the month from current date

#next 3 lines found here: https://www.studytonight.com/python-howtos/how-to-get-month-name-from-month-number-in-python
import calendar
current_month = calendar.month_name[current_month_number] #get the month name from the month number
current_month_abbr = calendar.month_abbr[current_month_number] #get the abbreviation

#convert to uppercase so user entry can be case insensitive
#see if this month is birthday month, print bday message if true
if month.upper() == current_month.upper() or month.upper() == current_month_abbr.upper():
    print('Happy birthday month!')

#note to self: go to strftime library for different method 