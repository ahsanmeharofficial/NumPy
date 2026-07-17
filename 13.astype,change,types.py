#astype is a method that is use to change the data type of arry 

import numpy as np 
arr=np.array([1.1, 2.2, 3.0])
print(arr.dtype)# curently float 
int_arr = arr.astype (int) # method convert into intger value

print (int_arr)
print(int_arr.dtype)  