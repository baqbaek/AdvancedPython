import string

def pig_it(text):
    x = text.split()
    for i in range(len(x)):
        if x[i] not in string.punctuation:
            x[i] = x[i][1:] + x[i][0] + 'ay'

    return ' '.join(x)

print(pig_it('hello'))