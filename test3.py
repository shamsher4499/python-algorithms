
# list_data = [1,2,3,4,5,6]
# n = 3
# l = 5
# # output = [1,2,6,5,4,3]
# # output = [1,6,5,4,3,2]
# new_list = list_data[:n-1]+list_data[n-1:][::-1]
# print(new_list)

# new_str = 'shamsher singh chauhan'
# def count_str(string_data:str):
#     count = 0
#     for i in string_data:
#         if i in ['s']:
#             count += 1

#     return count

# print(count_str(new_str))

# def find_target(list_data, target):
#     for i,j in enumerate(list_data):
#         if target==j:
#             return i
#     else:
#         return -1

# print(find_target(list_data,n))

# from bisect import bisect_left, insort

# def add_value_right_position(list_data:list, target:int) -> list:
#     # list_data.insert(bisect_left(list_data, target), target)
#     insort(list_data, target)
#     return list_data

# print(add_value_right_position(list_data, n))


'''
*
* *
* * *
* * * *
* * * * *
'''

# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print('\n')


# def missing_number(list_data):
#     counting = list(range(len(list_data)+1))
#     for i in list_data:
#         counting.remove(i)
#     return counting[0]
        

# data = [0,1,3,4, 5, 2, 7]
# print(missing_number(data))

# list_data = [1,2,3,4,5,6,7,8,9,10]
# start = 3
# end = 5
# output = [1,2,6,5,4,3]
# output = [1,2,5,4,3,6,7,8,9,10]
# new_list = list_data[:start-1]+list_data[start-1:end][::-1]+list_data[end:]
# print(new_list)
    
# un_sorted_list = [[3,4,1],[2,5,6],[8,1,10]]

# len_list = len(un_sorted_list)
# k = 1
# for i in range(len_list):
#     for j in range(0, len_list-i-1):
#         if un_sorted_list[j][k] > un_sorted_list[j+1][k]:
#             un_sorted_list[j], un_sorted_list[j+1] = un_sorted_list[j+1], un_sorted_list[j]

# print(un_sorted_list)

# squares_generator = (x**2 for x in range(5))
# print(next(squares_generator))
# print(next(squares_generator))
# print(next(squares_generator))
# print(next(squares_generator))
# print(next(squares_generator))

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3

# for value in simple_generator():
#     print(value)

# Program to check if a number is prime or not

num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable
# flag = False

# if num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break

#     # check if flag is True
#     if flag:
#         print(num, "is not a prime number")
#     else:
#         print(num, "is a prime number")


