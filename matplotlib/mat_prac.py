from pylab import *
import matplotlib.pyplot as plt
import numpy as np
import math

t=np.arange(0,2.5,0.1)
y1=map(math.sin,math.pi*t)
y2=map(math.sin,math.pi*t+math.pi/2)
y3=map(math.sin,math.pi*t-math.pi/2)

plt.plot(t,y1,'b*',t,y2,'g^',t,y3,'ys')
plt.show()


