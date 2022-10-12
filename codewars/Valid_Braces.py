def valid_braces(string):
    open = '([{'
    data = ('()', '[]', '{}')

    temp = []
    for i in string:
        if i in open:
            temp.append(i)
        else:
            try:
                if any(i in x and temp[-1] in x for x in data):
                    del temp[-1]
            except:
                return False

    return not temp
        


print(valid_braces('('))