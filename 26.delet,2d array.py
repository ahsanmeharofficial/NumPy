#delet list by using  delet funtion 
import numpy as np
arr=np.array([[1,2,3],[3,4,5]])# list ka matrix hona zrori ha elements kam zayda na hon varna function ni chala ga 

newarr=np.delete(arr,0,axis=0)#0 index vali list ko delet ker numpy ma list k under sa delet possible ni 
print (newarr)