def sort_dict(d):
    return sorted([(k, v) for k, v in d.items()], key=lambda x: x[1])



print(sort_dict({3:1, 2:2, 1:3}))  # [(1,3), (2,2), (3,1)]
print(sort_dict({1:2, 2:4, 3:6}))  # [(3,6), (2,4), (1,2)]