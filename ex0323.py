#ステップ関数の描画
import numpy as np
import matplotlib.pyplot as plt

def step_function(x):
  
  return np.array(x>0,dtype=np.int)

x=np.arange(-0.5,0.5,0.1)
y=step_function(x)
plt.plot(x,y)
plt.ylim(-0.1,1.1)
plt.show()