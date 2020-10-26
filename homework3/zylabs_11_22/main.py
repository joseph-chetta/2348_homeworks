# Joseph Chetta 1640405


if __name__ == '__main__':
    word_dict = {}
    words = input()
    words = words.split()
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    for word in words:
        print(word, word_dict[word])

