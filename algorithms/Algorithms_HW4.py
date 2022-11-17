"""
Even First
Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
You are required to solve it without allocating additional storage (operate with the input list).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
"""

#0(n)
def even_first(arr):
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0:
            next_even += 1
        else:
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1

test_list = [7, 3, 5, 6, 4, 10, 3, 2]
print(test_list)
even_first(test_list)
print(test_list)


"""
Increment a Number
Write a program that takes as input a list of digits encoding a non-negative decimal integer D 
and updates the list to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
"""

#0(n)
def plus_one(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1

    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

test_number_1 = [1, 2, 5] # -> [1. 2, 6]
test_number_2 = [1, 2, 9] # -> [1, 3, 0]
test_number_3 = [9, 9, 9] # -> [1, 0, 0, 0]

print(plus_one(test_number_1))
print(plus_one(test_number_2))
print(plus_one(test_number_3))

