'''
input='tree'
output='eetr' or 'eert'

input='cccaaa'
output='aaaccc' or 'cccaaa'

input='Aabb'
output='bbAa' or 'bbaA'
'''

# def check_string(string:str) -> str:
#     dict_data = {}
#     for i in string:
#         if i in dict_data:
#             dict_data[i]+=1
#         else:
#             dict_data[i] = 1
#     data = dict(sorted(dict_data.items(), key=lambda x:x[1], reverse=True))
#     ch = ''
#     for key,value in data.items():
#         ch += key*value
#     return ch

from collections import Counter
def check_string(string: str) -> str:
    char_counts = Counter(string)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    result = ''.join(char * count for char, count in sorted_chars)
    return result

input='tree'
print(check_string(input))