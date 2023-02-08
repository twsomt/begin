test_lst = list(range(10000))


item = 67

def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
   
    while low <= high:
        mid = int((low + high) / 2)
        guess = lst[mid]
        if guess == item:
            return mid

        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(test_lst, item))
