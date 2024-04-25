import numpy as np

#-------array---arange-----

ar_arr = np.arange(1,10)

# note: arange(start, stop, step, dtype=None)

# print(ar_arr)

#output: create array from 1,10

# [1 2 3 4 5 6 7 8 9]

#----reshape the array---

re_arr = ar_arr.reshape((3,3))

# print(re_arr)

# output: convert array into 3 rows and 3 col
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

#------Flat Array-----

flat_arr = re_arr.flatten()

# print(flat_arr)

# output: convert array into 1D array----

# [1 2 3 4 5 6 7 8 9]

#----convert into original array-----

rev_arr = ar_arr.ravel()

# print(rev_arr)

#output: print original array
# [1 2 3 4 5 6 7 8 9]