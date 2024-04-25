

# def change_function(func):
#     def wrapper(*args, **kwargs):
#         data = func(*args, **kwargs)
#         return data.lower()
#     return wrapper

# @change_function
# def username():
#     return 'PYTHON'

# print(username())

list1 = [[1,2,3,6], [7,15,9,5], [15,-1,5,4]]
index_to_sort_by = 1

# sorted_list_data = sorted(list1, key=lambda x: x[index_to_sort_by])

# print(sorted_list_data)


# list1 = [2,15,-1]
# list1 = [2,-1,15]
for i in range(len(list1)):
    for j in range(0, len(list1)-i-1):
        if list1[j][index_to_sort_by] > list1[j+1][index_to_sort_by]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print(list1)