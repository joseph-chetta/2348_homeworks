# Joseph Chetta 1640405


if __name__ == '__main__':
    list_input = input()
    l = list_input.split(" ")
    values = []
    for i in l:
        if int(i) >= 0:
            values.append(int(i))
    values.sort()
    for i in values:
        print(i, end=' ')


