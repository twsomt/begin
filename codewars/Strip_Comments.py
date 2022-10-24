def strip_comments(strng, markers):
    print(strng)
    print(markers)
    

    res = []
    temp = []
    flag = True
    
    for i in strng:
        if i in markers:
            flag = False
        elif ord(i) == 10:
            flag = True
            res.append(temp)
            temp = []

        if flag:
            temp.append(i)
        
    res.append(temp)
    res = ''.join(list(map(lambda x: ''.join(x).rstrip(' \t'), res)))
    return res