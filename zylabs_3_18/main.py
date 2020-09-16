# Joseph Chetta 1640405

import math

print('Enter wall height (feet):')
wh = int(input())
print('Enter wall width (feet):')
ww = int(input())
area = wh * ww
print('Wall area: {} square feet'.format(area))

coverage = 350
paint_needed = area / coverage
print('Paint needed: %.2f gallons' % paint_needed)
cans_needed = math.ceil(paint_needed)
print('Cans needed: {} can(s)\n'.format(cans_needed))

print('Choose a color to paint the wall:')
color = input()

color_cost = {
    'red': 35,
    'blue': 25,
    'green': 23
}
total_cost = str(color_cost[color] * cans_needed)
print('Cost of purchasing {} paint: ${}'.format(color, total_cost))
