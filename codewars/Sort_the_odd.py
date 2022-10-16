def sort_array(source_array):
    odds = sorted([n for n in source_array if n % 2 != 0])
    for n in source_array:
        if n % 2 == 0:
            odds.insert(source_array.index(n), n)
    return odds

print(sort_array([1, 3, 2, 5, 4, 7, 6, 9, 8, 0]))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

