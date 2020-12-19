# import time
# import sys
import os
import pandas

# print(sys.builtin_module_names)
# print(sys.prefix)

# while True:
    # file_dir = './texts/fruits.txt'
    # if os.path.exists(file_dir):
    #     with open(file_dir) as file:
    #         print(file.read())
    # time.sleep(5)

file_dir = './texts/temps.csv'
if os.path.exists(file_dir):
    data = pandas.read_csv(file_dir)
    print(data)
    print(type(data))
    data_mean = data.mean()
    print(data_mean)

