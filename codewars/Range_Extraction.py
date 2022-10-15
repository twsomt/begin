def approx_equals(a, b):
    return a == b or -1 <= a - b <= 1

def cut_temp(temp, res):
    if len(temp) < 3:
        for x in temp:
            res.append(x)
    else:
        res.append(temp)
    return res

def solution(args):
    temp = []
    res = []
    for i in args:
        if not temp:
            temp.append(i)
        else:
            if approx_equals(temp[-1], i):
                temp.append(i)
            else:
                cut_temp(temp, res)

                temp = []
                temp.append(i)

    cut_temp(temp, res)

    return ','.join([str(i) if type(i) == int else f'{i[0]}-{i[-1]}' for i in res])


print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 27]))






#"-10--8,-6,-3-1,3-5,7-11,14,15,17-20"