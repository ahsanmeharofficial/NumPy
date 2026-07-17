#slicing is base on (start, stop, steps)


import numpy as np
arr = np.array ([10,20,30,40,50,60])

print (arr [0:3]) #start with  zero index to 5   last element ko count ni kerta like 1 to 5 it print till 0 to 4
print (arr [1:5])#index 0 to 4
print (arr [0:4])#index zero to 3
print (arr [::2])#EVERY 2 ELEMENT 
print (arr [::-1]) #reverse the array 