fib = lambda x : 1 if x <= 2 else fib(x - 1) + fib(x - 2)
print(fib(31))


numbers = [1, 2, 3]
words = ['one', 'two', 'three']

for pair in zip(numbers, words):
    print(pair)


x = zip(numbers, words)
print(list(x))
