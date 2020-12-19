import json
from difflib import get_close_matches

with open('data.json') as file:
    data = json.load(file)

def getDefinations(key):
    l_key = key.lower()
    t_key = key.title()
    u_key = key.upper()
    if key in data:
        return data[key]
    if t_key in data:
        return data[t_key]
    if u_key in data:
        return data[u_key]
    if l_key in data:
        return data[l_key]

    matches = get_close_matches(l_key, data.keys(), n=1, cutoff=0.7)
    if len(matches) > 0:
        ans = input('Did you mean \'{}\' instead? Enter y if yes or n if no: '.format(matches[0]))
        while ans.lower() != 'n':
            if ans.lower() == 'y':
                return data[matches[0]]
            ans = input('Please enter y or n ')

    return 'The word doesn\'t exists. Please double check it.'

#print(len(data))
#print(type(data))

while True:
    user_input = input('Enter term: ')
    if user_input == '/end': break
    definations = getDefinations(user_input)
    if isinstance(definations, list):    
        for defination in definations:
            print(defination)
    else:
        print(definations)
