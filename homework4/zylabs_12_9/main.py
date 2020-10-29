# Joseph Chetta 1640405

if __name__ == '__main__':
    line = None
    while line != '-1':
        line = input()
        if line == '-1':
            break
        line = line.split()
        name = line[0]
        try:
            age = int(line[1]) + 1
        except:
            age = 0
        print('{} {}'.format(name, age))
