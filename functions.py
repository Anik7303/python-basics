def mean(value):
    #if type(value) == list:
    if isinstance(value, list):
        return sum(value) / len(value)
    #elif type(value) == dict:
    elif isinstance(value, dict):
        return sum(value.values()) / len(value)

print(mean([1, 2, 3]))
print(mean({'x':10, 'y':20, 'z':30}))