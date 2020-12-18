# my_file = open('fruits.txt');
# file_content = my_file.read();
# my_file.close()

# better way
with open('./texts/fruits.txt') as my_file:
    file_content = my_file.read()

print(file_content)

# write to file, and if file exists write over it
with open('./texts/giberis.txt', 'w') as my_file:
    my_file.write('alsjnbsdlfja\najsdf;ljnasdljasdf')
    my_file.write('\nlajsdlf\nlja;sldfj')

# write to file, but if file exists append to its end
with open('./texts/giberis.txt', 'a') as my_file:
    my_file.write('\nnew giberis.....')

# both read and write to file with append functionality
with open('./texts/giberis.txt', 'a+') as my_file:
    my_file.write('\nagain some new giberis.....')
    my_file.seek(0) # move cursor to start position
    file_content = my_file.read()

print(file_content)