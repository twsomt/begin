file = open('nums.txt')

print(sum(map(int, file.read().split())))

file.close()