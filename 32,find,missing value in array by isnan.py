#by using isnan funtion  we use to find the empty value  but it return bolean answer
import numpy as np
arr = np.array([1,2,np.nan ,3])  # where we palce np.nan it print ture 
print (np.isnan(arr))

# this function is only use to find missing values 