#to get current date and time 
# we need to use the datetime library
from datetime import datetime, timedelta
today = datetime.now()
print('Today is: ' + str(today))
#timedelta is used to add or subtract days, hours, minutes, seconds, etc.
#  from a date
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))
print('day: ' + str(today.day))
print('month: ' + str(today.month))
print('year: ' + str(today.year))
#.year, .month, and .day are attributes of the datetime object
#  that return the year, month, and day of the date, respectively.

print('Today is:' + str(today.strftime('%A, %B %d, %Y')))
#.strftime() is a method of the datetime object that formats the 
# date as a string according to the specified format codes. In this case,
#  %A returns the full weekday name, %B returns the full month name, 
# %d  returns the day of the month as a zero-padded decimal number, and
#  %Y returns the year with century as a decimal number.
birthday = input('when is  your birthday: (dd/mm/yyyy) ')
# we can use the strptime() method to convert a string to
#  a datetime object
#birthday_date = datetime.strptime(birthday, '%Y-%m-%d')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Your birthday is: ' + str(birthday_date))
print('Your birthday is: ' + str(birthday))
birthday_eve = birthday_date - one_day
print('Your birthday eve is: ' + str(birthday_eve))
