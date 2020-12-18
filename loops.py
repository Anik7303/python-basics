# for loop
temperatures = [9.1, 8.8, 7.5]

for temperature in temperatures:
    print(round(temperature))

for letter in 'Hello world':
    print(letter)

grades = { 'marry': 9.1, 'sam': 8.8, 'john': 7.5}

for item in grades.items():
    print(item)

for key, value in grades.items():
    print('key: {} | value: {}'.format(key, value))

for name in grades.keys():
    print(name)

for grade in grades.values():
    print(grade)

count = 0
while count < 10:
    print(count)
    count = count + 3

import datetime
while datetime.datetime.now() < datetime.datetime(2020, 12, 18, 22, 28):
    print('not yet')
