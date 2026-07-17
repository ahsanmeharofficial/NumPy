#insert function has desegn to upadete the array by your desiser value 
#insert(array, index  , vulue , axies )
# axies =0 mean row wise  And at 1 is colum wise 
import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr)#orignal print 
arr_updt=np.insert(arr,2,100,axis=0) #at 2nd index   
print(arr_updt)