
from itertools import zip_longest
from typing import final

def counter_letters(x, num):
    cnt_letters = []
    used_letters = []
    for i in x:
        y = x.count(i)
        if y > 1 and (i, y) not in cnt_letters and i not in used_letters:
            cnt_letters.append((i, y, num+1))

    return cnt_letters

def mix(s1, s2):
    res_count = []
    for i in range(2):
        x = tuple(filter(lambda x: x.isalpha() and x.islower() ,(s1, s2)[i]))
        res_count.append(counter_letters(x, i))

    r1 = []
    r2 = []
    


    for x, y in zip_longest(res_count[0], res_count[1], fillvalue=('0', 0, '=')):
        r1.append(x)
        r2.append(y)
    r1 = sorted(r1, key=lambda x: x[1], reverse=True)
    r2 = sorted(r2, key=lambda x: x[1], reverse=True)
    letters = []
    tags_lem = []
    r1_letters = []
    r2_letters = []
    
    for x, y in zip(r1, r2):
        # print(f'{x}{y}')
        r1_letters.append(x[0])
        r2_letters.append(y[0])

        if x not in tags_lem:
            letters.append(x[0])
            tags_lem.append([x[0], x[1], x[2]])
            
        if y not in tags_lem:
            letters.append(y[0])
            tags_lem.append([y[0], y[1], y[2]])
            

    queue = []
    # for i in 

    # print(letters)
    tags_lem = [i for i in tags_lem if i[0] != "0"]
    sorted_tags_lem  = sorted(tags_lem, key=lambda x: x[1], reverse=True)
    # [print(i) for i in sorted_tags_lem]
    
    # print(r1_letters)
    # print(r2_letters)
    
    cop = sorted_tags_lem


    for i in range(len(cop)):
        if s1.count(cop[i][0]) == s2.count(cop[i][0] ):
            sorted_tags_lem[i][-1] = '='
    # print()
    # [print(i) for i in sorted_tags_lem]
    res = []
    for i in sorted_tags_lem:
        if i not in res:
            res.append(i)
    
    d_res = dict()
    for i in res:
        if i[0] in d_res:
            if d_res[i[0]][1] < i[1]:
                d_res[i[0]] = i
        else:
            d_res[i[0]] = i


    
    # print(len(d_res))

    res = list(map(lambda x: tuple(x), d_res.values()))
    res.sort(key=lambda x: (x[1]), reverse=True)
    
    temp_1 = []
    temp_2 = []

    res_1 = res
    for i in res_1:
        if i[2] == '=':
            temp_1.append(i)
        elif i[1] == 2:
            temp_2.append(i)
            
    res_1 = [i for i in res if i[2] != '=']
    res_1 = [i for i in res_1 if i[1] != 2]
    
    temp_1 = sorted(temp_1, key=lambda x: x[0])
    temp_2 = sorted(temp_2, key=lambda x: x[0])
    # print(res_1)
    # print(temp_2)
    # print(temp_1)
    res = res_1 + temp_2 + temp_1
    # print(res)
    


    [print(i) for i in res]
    print()
    print()
    x = sorted(res, key=lambda x: x[1], reverse=True)


    x_res = []
    n = len(set([i[1] for i in x]))

    for _ in range(n):
        temp = []
        y = x[0][1]
        yy = 0
        cnt = 0
        while True:
            yy = y
            try:
                y = x[cnt][1]
            except:
                break
            
            if y != x[0][1]:
                break
            
            temp.append(x[cnt])
            cnt += 1
            
        temp_1 = sorted([i for i in temp if i[-1] != '='], key=lambda x: (x[-1], x[0]))
        temp_2 = sorted([i for i in temp if i[-1] == '='], key=lambda x: (x[-1], x[0]))
        temp = temp_1 + temp_2
        x_res += temp
        
        x = [i for i in x if i[1] != yy]


    [print(i) for i in x_res]

    res_2 = [f'{i[2]}:{i[0]*i[1]}' for i in x_res]
    res_3 = '/'.join(res_2)



    return res_3



print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))# "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"



# s1 = "A aaaa bb c"
# s2 = "& aaa bbb c d"
# s1 имеет 4 'a', 2 'b', 1 'c'
# s2 имеет 3 'a', 3 'b', 1 'c', 1 'd'
