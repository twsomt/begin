print(all(lambda x: x.isnumeric() for x in 'aa.bb.cc.dd'.split('.')))
# True

print(all(x.isnumeric() for x in 'aa.bb.cc.dd'.split('.')))
# True

x = 'ab'
print(list(map(lambda x: x.isnumeric(), 'aa.bb.cc.dd'.split('.'))))
# [False, False, False, False]



h = 'fff'
print(lambda x: x.isnumeric())