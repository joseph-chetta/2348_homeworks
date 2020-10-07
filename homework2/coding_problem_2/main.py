# Joseph Chetta 1640405

# Portion 'b' solution
file = 'inputDates.txt'
with open(file) as file_data:
    for line in file_data:
        if line == '-1':
            break
        t = line.find('March 1, 1990')
        if not t:
            print('3/1/1990')
        else:
            # ignore
            pass


