given_array = [1, 2, 3, 4, 5, 6, 7]
k = 3
# Output: [5, 6, 7, 1, 2, 3, 4]

new_array = given_array[-k:] + given_array[:-k]
print(new_array)