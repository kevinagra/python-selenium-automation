"""
Below The Arithmetical Mean
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
"""

#0(n)
def below_arithmetical_mean(arr):
    arithmetical_mean = sum(arr) / len(arr)
    result_list = []
    for i in arr:
        if i < arithmetical_mean:
            result_list.append(i)
    return result_list

test_list = [1, 3, 5, 6, 4, 10, 2, 3] # am = 4.25
result = below_arithmetical_mean(test_list)
print(result)  # [1, 3, 4, 2, 3]


"""
Two Lowest Elements
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
"""

#0(1)
def two_lowest_elements(arr):
    arr.sort()
    return arr[:2]

test_list = [198, 3, 4, 9, 10, 9, 2] # [2, 3]
result = two_lowest_elements(test_list)
print(result)

