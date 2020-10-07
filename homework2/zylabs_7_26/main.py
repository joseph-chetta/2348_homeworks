# Joseph Chetta 1640405

def exact_change(user_total):
    if user_total >= 100:
        num_dollars = int(user_total / 100)
        user_total %= 100
    else:
        num_dollars = 0

    if user_total >= 25:
        num_quarters = int(user_total / 25)
        user_total %= 25
    else:
        num_quarters = 0

    if user_total >= 10:
        num_dimes = int(user_total / 10)
        user_total %= 10
    else:
        num_dimes = 0

    if user_total >= 5:
        num_nickels = int(user_total / 5)
        user_total %= 5
    else:
        num_nickels = 0

    num_pennies = user_total

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies

if __name__ == '__main__':
    total = int(input())

    if total <= 0:
        print('no change')

    dollars, quarters, dimes, nickels, pennies = exact_change(total)

    if dollars > 1:
        print("{} dollars".format(dollars))
    elif dollars == 1:
        print("{} dollar".format(dollars))

    if quarters > 1:
        print("{} quarters".format(quarters))
    elif quarters == 1:
        print("{} quarter".format(quarters))

    if dimes > 1:
        print("{} dimes".format(dimes))
    elif dimes == 1:
        print("{} dime".format(dimes))

    if nickels > 1:
        print("{} nickels".format(nickels))
    elif nickels == 1:
        print("{} nickel".format(nickels))

    if pennies > 1:
        print("{} pennies".format(pennies))
    elif pennies == 1:
        print("{} penny".format(pennies))
