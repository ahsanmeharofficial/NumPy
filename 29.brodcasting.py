#without loops apply discount and other pernecATEGES  on array 
import numpy as np 
prices= np.array([100,200,300])

discount=10

finalprice= prices - (prices*discount/100)
print(finalprice)

#without loops in less line of codes 