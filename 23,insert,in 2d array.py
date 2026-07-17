#2d array ma dATA KO  insert kerna row wsie and colum wise 
import numpy as np 
arr=np.array ([[1,2],[3,4]])#2d array

new_arr= np.insert(arr,2,[10,11],axis=1) #axies = 0 (row),1(colume),none( 1d array )
print(new_arr)