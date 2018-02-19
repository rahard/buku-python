import numpy as np
import matplotlib.pyplot as plt

f = open('data.txt', 'r')

x = []
y = []
while True:
   line = f. readline()
   if not line: 
       break
   line = line.rstrip()
   a,b = line.split(',')
   x.append(int(a))
   y.append(int(b))

plt.plot(x,y,'o',label='Random Data')
plt.legend()
plt.show()
