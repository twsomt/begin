def sum_of_intervals(intrvls):
    if not intrvls:
        return 0
    else:
        intrvls.sort()
        res = []
        strt, fnsh = intrvls[0][0], intrvls[0][1]
        
        for i, interval in enumerate(intrvls[1:]):
            f, d = interval[0], interval[1]
            if f > fnsh:
                res.append([strt, fnsh])
                strt, fnsh = f, d
            else:
                fnsh = max(d, fnsh)
        res.append([strt, fnsh])
    return sum(map(lambda x: x[-1] - x[0], res))


# print(sum_of_intrvls([(1, 5), (6, 10)]))