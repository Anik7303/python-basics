import datetime

def get_sqrt(num):
    return num**(1/2)

def isPrime(num):
    if num < 2 or num % 2 == 0:
        return False
    #for x in range(3, num, 2):
    x = 3
    limit = num ** 1/2
    while x <= limit:
        if num % x == 0:
            return False
        x = x + 2

    return True

def test(num):
    if isPrime(num):
        print('{} is a prime number'.format(num))
    else:
        print('{} is not a prime number'.format(num))

while True:
    user_input = input('Enter a number: ')
    if user_input == 'end':
        break
    test(int(user_input))

# user_input = input('Search for primes from 1 to ')
# #print(datetime.datetime.now())
# primes = [x for x in range(1, int(user_input)) if isPrime(x)]
# #print(datetime.datetime.now())
# print(len(primes))
