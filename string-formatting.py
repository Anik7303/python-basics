numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
print(numbers[1:4]) # from index 1 to 3

print(numbers[:5]) # from start index to index 4

print(numbers[-2:]) # last two

print(numbers[-4:]) # last 4 elements

print(numbers[-1]) # last element

text = 'hello world'
print(text[1:4]) # from second letter to 4th letter

print(text[:5]) # from first letter to 5th letter

print(text[-2:]) # last two letter

print(text[-4:]) # last 4 letters

print(text[-1]) # last letter

firstname = input('Enter your firstname: ')
lastname = input('Enter your lastname: ')
count = 1

message = '%d. Hello, %s %s' % (count, firstname, lastname)

count = count + 1
# only works for python version >3.6
another_message = f'{count}. Hi, {firstname} {lastname}'

count = count + 1
third_message = '{}. Hello, {}. How are you?'.format(count, firstname);

print(message, another_message, third_message)
