
#method 1

# def fibonacci(num:int):
#     if num < 0:
#         return 'Incorrect value'
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     return fibonacci(num-1)+fibonacci(num-2)

# print(fibonacci(9))

#method 2

# 1 2 3 5 8 13

def fibonacci_series_number(num:int):
    list_data = [0,1]
    if num < 0:
        return 'Incorrect value'
    if num == 0:
        return 0
    elif num == 1:
        return 1
    while len(list_data) < num:
        data = list_data[-1] + list_data[-2]
        list_data.append(data)
    return list_data


print(fibonacci_series_number(3))