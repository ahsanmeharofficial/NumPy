#it change the shape of aray to convert it into a 1d to 2d  and 3d so that 
import numpy as np 
arr=np.array([1,2,3,4,5,6])
reshaped_Arr=arr.reshape(2,3)
print (reshaped_Arr)
#it convert 1d array in 2 d array like 2 rows and 3 colums 

#note it does not create copy it create view only 