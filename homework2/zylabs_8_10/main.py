# Joseph Chetta 1640405

def remove_space(string):
    return "".join(string.split())

def reversed_str(string):
    rev_str = ''
    for char in reversed(string):
        rev_str += char
    return rev_str

def palindrome(str):
    # Remove space before reversing str
    str = remove_space(str)
    rev_str = reversed_str(str)
    if str == rev_str:
        return True
    else:
        return False


str = input()
if palindrome(str):
    print("{} is a palindrome".format(str))
else:
    print("{} is not a palindrome".format(str))

