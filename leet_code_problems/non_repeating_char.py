'''
input = 'leetcode'
output = 0

input = 'aabb'
output = -1

input = 'loveleetcode'
output = 2
'''

def check_string(text: str) -> int:
    data = {}
    
    for index, char in enumerate(text):
        if char not in data:
            data[char] = index
        else:
            data.pop(char)
    return sorted(data.values())[0] if data else -1


input = 'aabb'
print(check_string(input))