'''
input=['flower', 'flow', 'flight']
output='fl'

input=['dog', 'racecar', 'car]
output=''
'''

def longest_substring(str_list):
    sort_list = sorted(str_list, key=len)
    check = sort_list[0]
    for index, value in enumerate(check):
        for index1, value1 in enumerate(sort_list):
            print(index, value, index1, value1)
            # if value != value1[index]:
                
            

    
input=['flower', 'flow', 'flight']
print(longest_substring(input))