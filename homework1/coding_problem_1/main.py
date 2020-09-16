# Joseph Chetta 1640405

from datetime import date

print('Enter the current month:')
current_month = int(input())
print('Enter the current day:')
current_day = int(input())
print('Enter the current year:')
current_year = int(input())
current = date(current_year, current_month, current_day)

print('')
print('Enter your birthday month:')
bday_month = int(input())
print('Enter your birthday day:')
bday_day = int(input())
print('Enter your birthday year:')
bday_year = int(input())
bday = date(bday_year, bday_month, bday_day)

age = current.year - bday.year - ((current.month, current.day) < (bday.month, bday.day))
if (current_day == bday_day) and (current_month == bday_month):
    birthday = True
else:
    birthday = False
print('')
print('')
print('Bithday Calculator')
print('Current day')
print('Month:', str(current_month))
print('Day:', str(current_day))
print('Year:', str(current_year))
print('Birthday')
print('Month:', str(bday_month))
print('Day:', str(bday_day))
print('Year:', str(bday_year))
if birthday:
    print('Happy Birthday!')
print('You are {} years old.'.format(str(age)))


