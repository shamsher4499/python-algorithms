'''
Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

def remove_duplicate_number(list_data) -> int:
    new_list = []
    new_commas = []
    for i in list_data:
        if i not in new_list:
            new_list.append(i)
        else:
            new_commas.append('_')
    new_list.extend(new_commas)
    return new_list

nums = [0,0,1,1,1,2,2,3,3,4]
# print(nums)
print(remove_duplicate_number(nums))