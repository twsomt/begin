def next_bigger(i):
    x: list = list(str(i))
    y = int(''.join(map(str, sorted(x, reverse=True))))
    z = int(''.join(map(str, sorted(x))))
    my_i = i
    while my_i <= y:
        my_i += 1
        if int(''.join(map(str, sorted(list(str(my_i)))))) == z:
            return my_i
    else:
        return -1

print(next_bigger(12))    #    21
print(next_bigger(21))    #    -1
print(next_bigger(513))   #   531
print(next_bigger(2017))  #  2071
print(next_bigger(414))   #   441
print(next_bigger(144))   #   414