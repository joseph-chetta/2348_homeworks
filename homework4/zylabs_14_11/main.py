# Joseph Chetta 1640405

def selection_sort_descend_trace(int_list):
    for i in range(len(int_list)):
        max_idx = i
        for j in range(i+1, len(int_list)):
            if int_list[max_idx] < int_list[j]:
                max_idx = j
        int_list[i], int_list[max_idx] = int_list[max_idx], int_list[i]
        if i != len(int_list) - 1:
            for num in int_list:
                print(num, end=' ')
            print('')


if __name__ == '__main__':
    l = input()
    int_list = []
    for num in l.split():
        int_list.append(int(num))
    selection_sort_descend_trace(int_list)
