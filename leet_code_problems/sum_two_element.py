def sum_two_element(nums:list[int], target:int)->list[int]:
    temp_dict = {}
    for index,num in enumerate(nums):
        complement = target-num

        if complement in temp_dict:
            return [temp_dict[complement],index]
        
        temp_dict[num]=index

num_list=[1,2,3,4]
target=7
print(sum_two_element(num_list, target))