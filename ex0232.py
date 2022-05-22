import numpy as np
#and
def AND(x1,x2):
  x=np.array([x1,x2])
  w=np.array([0.5,0.5])
  b=-0.7
  tmp=np.sum(w*x)+b
  if tmp<=0:
    return 0
  else:
    return 1

print(AND(0,0))
print(AND(0,1))
print(AND(1,1))

#nand
def NAND(x1,x2):
  x=np.array([x1,x2])
  w=np.array([-0.5,-0.5])
  b=0.7
  tmp=np.sum(x*w)+b
  if tmp<=0:
    return 0
  else:
    return 1

print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,1))

#or
def OR(x1,x2):
  x=np.array([x1,x2])
  w=np.array([0.5,0.5])
  b=-0.2
  tmp=np.sum(x*w)+b
  if tmp>=0:
    return 1
  else:
    return 0

print('or')
print(OR(0,0))
print(OR(0,1))
print(OR(1,1))

#xor

def XOR(x1,x2):
  s1=NAND(x1,x2)
  s2=OR(x1,x2)
  y=AND(s1,s2)
  return y

print('xor')
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1)) 


