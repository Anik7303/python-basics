#import datetime
#print(datetime.datetime.now())

# lists type(temperatue)
temperatures = [32.4, 20.1, 16.7]

# dictionaries
grades = { 'marry': 9.1, 'sam': 8.3, 'john': 8.7}

# tuples
names = ('marry', 'sam', 'john')

mean_temperature = sum(temperatures)
mean_grade = sum(grades.values())

avg_temperature = mean_temperature / len(temperatures)
avg_grade = mean_grade / len(grades)

#print(mean_temperature, avg_temperature, mean_grade,avg_grade, names)


