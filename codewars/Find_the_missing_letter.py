import string
a = list(string.ascii_lowercase.lower())

def find_missing_letter(chars):
    x = set(a[a.index(chars[0].lower()):a.index(chars[-1].lower()) + 1]) - set([i.lower() for i in chars])
    print(x)

    if any(i.isupper() for i in chars):
        return list(x)[0].upper()
    else:
        return list(x)[0]

print(find_missing_letter(['O','Q','R','S']))


a = "a"
print(a.isupper())



# def find_missing_letter(chars):
#     n = 0
#     while ord(chars[n]) == ord(chars[n+1]) - 1:
#         n += 1
#     return chr(1+ord(chars[n]))