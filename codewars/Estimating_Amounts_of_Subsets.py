def est_subsets(arr):
    combination_count = 2**len(arr)
    res = []
    for i in range(0, combination_count):   
        tmp_str = str(bin(i)).replace("0b", "")
        tmp_lst = [int(x) for x in tmp_str]

        while (len(tmp_lst) < len(arr)):
            tmp_lst = [0] + tmp_lst

        subset = list(filter(lambda x : tmp_lst[arr.index(x)] == 1, arr))
        res.append(subset)

    return len(res) - 1
