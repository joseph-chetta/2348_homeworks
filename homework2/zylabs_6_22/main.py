# Joseph Chetta 1640405

def solutions_list(co1, co2, total):
    lst = []
    for i in range(-10, 11):
        for j in range(-10, 11):
            if (i * co1) + (j * co2) == total:
                lst.append("{} {}".format(i, j))
    return lst

co1 = int(input())
co2 = int(input())
total = int(input())
solution1 = solutions_list(co1, co2, total)

co1 = int(input())
co2 = int(input())
total = int(input())
solution2 = solutions_list(co1, co2, total)

no_solution = True
for sol in solution1:
    if sol in solution2:
        no_solution = False
        print(sol)

if no_solution:
    print('No solution')
