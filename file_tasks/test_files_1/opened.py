file = open('test.txt')
x = list(file.readline())
letters = []

for i in range(len(x)):
    if not x[i].isnumeric():
        letters.append(x[i]) 
        x[i] = ' '

nums = list(map(int, (''.join(x)).split()))

for i in range(len(nums)):
    print(letters[i] * nums[i], end='')