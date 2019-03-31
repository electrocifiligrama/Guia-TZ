import math
import numpy as np


H7= np.array( [ [12,10,8,6,4,2,2], [5,10,8,6,4,3,1], [4,3,8,6,5,3,2],
              [3,2,1,7,5,4,3], [2,1,1,0,6,5,4], [1,1,0,0,0,6,5], [1,0,0,0,0,0,6] ])

H5= np.array( [ [10,8,6,4,3], [3,8,6,5,3], [2,1,7,5,4], [1,1,0,6,5], [1,0,0,0,6] ] )

H3= np.array( [ [8,6,5], [1,7,5], [1,0,6] ] )

delta3= np.linalg.det(H3)
delta5= np.linalg.det(H5)
delta7= np.linalg.det(H7) 
print("delta 3 %f",delta3)
print("delta 5 %f",delta5)
print("delta 7 %f",delta7)