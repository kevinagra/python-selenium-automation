#Coding questions:

"""
Compute the sum of digits in all numbers from 1 to n.
When a function gets a number n, find the sum of digits in all numbers from 1 to n.
Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
"""
def sum_to_n(n):
    final_sum = 0
    for x in range(n + 1): #range(start, stop, step)
        final_sum += x

    return final_sum

number = int(input('Input a number: '))
test_result = sum_to_n(number)  #5, 15
print('Result: ' + str(test_result))




"""
Find max number from 3 values.
Example: 124, 21, 32. Result = 124.
"""
def find_max(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3

n1 = int(input('Input number 1: '))
n2 = int(input('Input number 1: '))
n3 = int(input('Input number 1: '))

test_result = find_max(n1,n2,n3)
print('The biggest number is ' + str(test_result))
print(f'The biggest number is {test_result}')




"""
Count odd and even numbers. 
Count odd and even digits of the whole number.
Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
"""
def count_even_and_odd(n):
    odds = 0
    evens = 0

    while n != 0:
        current_number = n % 10
        if current_number % 2:
            odds += 1
        else:
            evens += 1
        n = n // 10

    return [odds, evens]

test_number = 56219 # odds: 3, evens: 2
test_result = count_even_and_odd(test_number)
print(test_result)




"""
Difference between modulus and floor division:
"""
number = 123
mod_result = number % 10 #123 / 10 = 12.3 | 123 % 10 =3
floor_res = number // 10 #123 / 10 = 12.3 | 123 // 10 = 12

print('mod_result: ' + str(mod_result))
print('floor_res: ' + str(floor_res))

