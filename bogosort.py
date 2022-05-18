# Болотная сортировка
from random import shuffle

def is_sort(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True

def bogosort(nums):
    while not is_sort(nums):
        shuffle(nums)
        print(*nums)
    return nums

numbers = list(range(10))
shuffle(numbers)
print(numbers)

sorted_numbers = bogosort(numbers)

print(sorted_numbers)