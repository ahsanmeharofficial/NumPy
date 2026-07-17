# nan to  num function is used to replace the value with  missing value 
import numpy as np
arr = np.array([1,2,np.nan ,3]) 

newarr= np.nan_to_num(arr,nan=99)  #iff u dont pass any value to nan=  so it decfultly pass 0
print (newarr)
