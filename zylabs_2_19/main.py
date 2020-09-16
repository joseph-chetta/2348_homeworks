# Joseph Chetta 1640405

print('Enter amount of lemon juice (in cups):')
lemon_juice = float(input())
print('Enter amount of water (in cups):')
water = float(input())
print('Enter amount of agave nectar (in cups):')
agave = float(input())
print('How many servings does this make?')
servings = float(input())

print('')
print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar\n'.format(agave))

print('How many servings would you like to make?')
desired_servings = float(input())

print('')
multiplier = desired_servings / servings
print('Lemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice * multiplier))
print('{:.2f} cup(s) water'.format(water * multiplier))
print('{:.2f} cup(s) agave nectar\n'.format(agave * multiplier))

print('Lemonade ingredients - yields {:.2f} servings'.format(desired_servings))
print('{:.2f} gallon(s) lemon juice'.format((lemon_juice * multiplier) / 16))
print('{:.2f} gallon(s) water'.format((water * multiplier) / 16))
print('{:.2f} gallon(s) agave nectar'.format((agave * multiplier) / 16))
