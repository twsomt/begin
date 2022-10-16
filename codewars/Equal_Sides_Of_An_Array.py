def find_even_index(arr):
    for i in range(len(arr)):
        print(f'{sum(arr[i:])} | {sum(arr[:i+1])}')
        if sum(arr[i:]) == sum(arr[:i+1]):
            return i
    return -1

print(find_even_index([0,0,0,0,0]))
