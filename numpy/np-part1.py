import numpy as np

#-------define---array------

arr1 = np.array([1,2,3])

#-----------1D-----------

arr2 = np.array([[1,2,3],[4,5,6]])

#------------2D------------

arr3 = np.array([[1,2,3],[4,5,6],[7,8,9]])

#-------------3D-------------

#--------Get-Size---------

# print(arr1.size)
# print(arr2.size)
# print(arr3.size)

#output:
# 3
# 6
# 9

#--------Get Shape---------

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)

#output:
# (3,)
# (2, 3)
# (3, 3)

#--------Get data present in array-------

# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)

#output: print int64 because all the element are integer
# int64
# int64
# int64

#--------Transpose array----------

# print(arr1.transpose())
# print(arr2.transpose())
# print(arr3.transpose())

#output:
# [1 2 3]

# [[1 4]
#  [2 5]
#  [3 6]]

# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]