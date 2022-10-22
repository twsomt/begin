snail_map = [[1,2,3, 5, 6],
         [4,5,6, 7, 8],
         [7,8,9, 9, 7]]
res = []
try:
    for _ in range(max([max(i) for i in snail_map])):
        [res.append(i) for i in snail_map[0]]
        snail_map = snail_map[1:]
        n = len(snail_map)
        m = len(snail_map[0])
        snail_map = [[snail_map[j][i] for j in range(n)] for i in reversed(range(m))]
except:
    print(res)
