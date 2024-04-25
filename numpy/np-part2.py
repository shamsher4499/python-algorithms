import numpy as np

#-----Empty Array------

emp_arr = np.empty((4,4), dtype=int)

# print(emp_arr)

#output: get empty array when dtype=int
# [[0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]
#  [0 0 0 0]]

#output: get empty array when dtype=float
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

#------create one array-----

one_arr = np.ones(4, dtype=int)

# print(one_arr)

#output: when dtype=float
# [1. 1. 1. 1.]

#output: when dtype=int
# [1 1 1 1]

#-----create 2D array----

two_arr = np.ones((2,4), dtype=int)

# print(two_arr)

#output:
# [[1 1 1 1]
#  [1 1 1 1]]

#-----create 3D array----

three_arr = np.ones((3,4), dtype=int)

# print(three_arr)

#output:
# [[1 1 1 1]
#  [1 1 1 1]
#  [1 1 1 1]]

#----create zero array-----

one_zero_arr = np.zeros((2,3), dtype=int)

# print(one_zero_arr)

#output:
# [[0 0 0]
#  [0 0 0]]