"""
Spilt in Half
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than
the second part.
E.g.: string = 'bbbbbcaaaaa'. Result = 'aaaaabbbbbc'.
"""

#O(1)
def split_in_half(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1

    left = s[:half + add]
    right = s[half + add:]
    return right + left

test_s_odd = 'aaaabbb'  #bbbaaaa
test_s_even = 'aaabbb'   #bbbaaa
print(split_in_half(test_s_even))
print(split_in_half(test_s_odd))


"""
Unique Characters in String
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False. 
"""

#O(n)
def uni_char(s):
#1
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)

    return True
#2
    #return len(set(s)) == len(s)

test_s_pos = 'abcde'
test_s_neg = 'aabcd'
print(uni_char(test_s_pos))  #True
print(uni_char(test_s_neg))  #False

