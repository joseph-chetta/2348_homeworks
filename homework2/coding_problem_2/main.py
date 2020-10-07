# Joseph Chetta 1640405

# Portion 'c' solution
import datetime

file = 'inputDates.txt'
with open(file) as file_data:
    for line in file_data:
        if line == '-1':
            break
        # remove the newline at end
        line = line.rstrip()
        format = '%B %d, %Y'
        try:
            date = datetime.datetime.strptime(line, format)
            new_date_format = "{}/{}/{}\n".format(date.month, date.day, date.year)
            with open('parsedDates.txt', 'a+') as file:
                file.write(new_date_format)
        except ValueError:
            print('Incorrect date format')

