x = 'Кошка'
def false_translate(x):
    return x[::-1].capitalize()

print(false_translate(x))

set1 = {'Yellow', 'Orange', 'Black'}
set2 = {'Orange', 'Blue', 'Pink'}

set1.difference_update(set2)
print(*set1)

x = {'a', 'b'}
print(x * 2)

# invisible commit