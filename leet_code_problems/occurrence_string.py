'''
Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.

'''

def find_sub_string_index(haystack:str, needle:str)-> int:
    sign = ''
    for _ in needle:
        sign += '_'
    for _ in haystack:
        if needle in haystack:
            haystack = haystack.replace(needle, sign)
    while haystack:
        for index,val in enumerate(haystack):
            if val == '_':
                return index
        return -1

data = "leetcode"
find = "leeto"
print(find_sub_string_index(data, find))