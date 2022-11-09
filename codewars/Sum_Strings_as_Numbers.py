# lol
# from gmpy2 import mpz
# def sum_strings(x, y):
#     return str(mpz(x or '0') + mpz(y or '0'))


def sum_strings(x, y):
    if (len(x) > len(y)):
        t = x
        x = y
        y = t
    res, x1, y1, tmp = "", len(x), len(y), 0
    x, y = x[::-1], y[::-1]

    for i in range(x1):
        sum = ((ord(x[i]) - 48) +
              ((ord(y[i]) - 48) + tmp))
        res += chr(sum % 10 + 48)
        tmp = int(sum / 10)
    for i in range(x1, y1):
        sum = ((ord(y[i]) - 48) + tmp)
        res += chr(sum % 10 + 48)
        tmp = (int)(sum / 10)
    if (tmp):
        res += chr(tmp + 48)
    res = res[::-1]
    if len(res) > 1 and res[0] == '0':
        res = res[1:]
    elif res == '':
        res = '0'
    return res
