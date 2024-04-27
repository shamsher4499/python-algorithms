'''
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

'''

def remove_element_from_list(nums, val) -> int:
    if not nums:
        return 0
    slow = 0
    fast = len(nums)-1
    while slow<=fast:
        if nums[slow] == val:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            fast -= 1
        else:
            slow += 1

    return slow

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_element_from_list(nums, val))