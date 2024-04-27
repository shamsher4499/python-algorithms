'''
Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''
import bisect

def search_insert_position(nums:list, target:int) -> int:
    last_value = nums[-1]
    if target > last_value:
        data = bisect.bisect_right(nums, target)
    else:
        data = bisect.bisect_left(nums, target)
    return data

value = [1,3,5,6]
target = 5
print(search_insert_position(value, target))