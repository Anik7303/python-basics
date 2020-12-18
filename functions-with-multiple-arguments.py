def mean_l(*args):
    # here args is a tuple
    return sum(args) / len(args)

print(mean_l(1, 2, 3, 4))

def mean_d(**kwargs):
    # here kwargs is a dictionary
    return sum(kwargs.values()) / len(kwargs);

print(mean_d(a=1, b=2, c=3, d=4))

def divide(a, b=2):
    return a/b

print(divide(10, 3))
print(divide(10))
print(divide(b=10, a=3))
