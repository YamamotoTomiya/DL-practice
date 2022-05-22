import numpy as np
x=np.array([1.0,0.5])
#1層目
w1=np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
b1=np.array([0.1,0.2,0.3])

a1=np.dot(x,w1)+b1
print(a1)
def sigmoid(x):
  return 1/(1+np.exp(-x))

z1=sigmoid(a1)
print(z1)
#2層目
w2=np.array([[0.1,0.4],[0.2,0.5],[0.3,0.6]])
b2=np.array([0.1,0.2])

a2=np.dot(z1,w2)+b2
z2=sigmoid(a2)
#3層目
def identify_function(x):
  return x

w3=np.array([[0.1,0.3],[0.2,0.4]])
b3=np.array([0.1,0.2])

a3=np.dot(z2,w3)+b3
y=identify_function(a3)
print(y)