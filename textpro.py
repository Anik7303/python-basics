inputs = []

def sentence_formatter(phrase):
    interogatives = ('why', 'how', 'what', 'when', 'who')
    if phrase.startswith(interogatives):
        return '%s?' % phrase.capitalize()
    return '%s.' % phrase.capitalize()

while True:
    user_input = input('Say something: ')
    if user_input == '\end':
        break
    inputs.append(sentence_formatter(user_input))

print(" ".join(inputs))