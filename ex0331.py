import numpy as np
A=np.array([[1,2],[3,4]])
np.ndim(A)
A.shape

B=np.array([[5,6],[7,8]])

x=np.dot(A,B)
print(x)