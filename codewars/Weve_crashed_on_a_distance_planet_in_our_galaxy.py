def is_leap_year(d, y):
    x = y / (1 / (d - round(d, 0)))
    return x == round(x, 0)

print(is_leap_year(124.125, 102))