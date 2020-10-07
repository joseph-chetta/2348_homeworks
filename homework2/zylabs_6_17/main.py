# Joseph Chetta 1640405

replace_char = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}
ending = 'q*s'

password = input()
new_pass = ''

for char in password:
    if char in replace_char.keys():
        new_pass += replace_char[char]
    else:
        new_pass += char

new_pass += ending
print(new_pass)
