# Joseph Chetta 1640405

from os import path
from csv import reader

def read_input(csv_reader):
    word_dict = {}
    for lines in csv_reader:
        word_arr = lines
        for word in word_arr:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    for word in word_dict:
        print(word, word_dict[word])


file = input()
with open(file) as csvfile:
    csv_reader = reader(csvfile, delimiter=',')
    read_input(csv_reader)