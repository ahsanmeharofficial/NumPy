#n matlb numbers dim matlb dimentions    1d 2d 3d etc

import numpy as np
arr1=np.array ([1,2,3,4])
arr2=np.array ([[1,2,3,4],[2,3,4,5]])
arr3=np.array ([[[1,2,3],[2,3,4],[5,3,5],[2,3,5]]])

print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)
#if u want to check 3d shape 
print(arr3.shape)# (1,4,3)  1 layar[] , 4 rows 3 colums 