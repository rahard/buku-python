import numpy as np
import matplotlib.pyplot as plt

a = 0.25
b = 0.75
jumlah_titik = 300

# buat dua list yang masih kosong
x_point = []
y_point = []

for i in range(jumlah_titik):
    x = np.random.normal(0.0,0.4)
    y = a*x + b + np.random.normal(0.0,0.1)
    x_point.append([x])
    y_point.append([y])

plt.plot(x_point,y_point,'o',label='Random Data')
plt.legend()
plt.show()
