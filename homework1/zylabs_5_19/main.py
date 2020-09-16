# Joseph Chetta 1640405

services = {
    'Oil change': 35,
    'Tire rotation': 19,
    'Car wash': 7,
    'Car wax': 12,
    '-': 0
}

print("Davy's auto shop services")
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')

print('Select first service:')
first_service = input()
first_service_cost = services[first_service]
print('Select second service:')
second_service = input()
second_service_cost = services[second_service]
total_cost = first_service_cost + second_service_cost

print('')
print("Davy's auto shop invoice\n")
if first_service == '-':
    print('Service 1: No service')
else:
    print('Service 1: {}, ${}'.format(first_service, str(first_service_cost)))
if second_service == '-':
    print('Service 2: No service\n')
else:
    print('Service 2: {}, ${}\n'.format(second_service, str(second_service_cost)))
print('Total: ${}'.format(str(total_cost)))
