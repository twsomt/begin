def pig_it(text):
    return ' '.join(list(map(lambda x: x[1:] + x[0] + 'ay' if (any(i.isalpha() for i in x)) else x,text.split())))