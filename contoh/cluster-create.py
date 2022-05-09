# membuat tiga cluster
# (cc) 2022, Budi Rahardjo
import numpy as np
import matplotlib.pyplot as plt

# buat function dulu
def buat_list(cx,cy):
   x_point.append([cx])
   y_point.append([cy])
   for i in range(jumlah_data):
      x = cx + np.random.normal(0.0,0.7)
      y = cy + np.random.normal(0.0,0.7)
      x_point.append([x])
      y_point.append([y])

jumlah_data=100
x_point = []
y_point = []
# cluster pertama, centroid di (10, 4,5)
buat_list(10.0, 4.5)
# cluster kedua, centroid di (3.5, 2.5)
buat_list(3.5, 2.5)
# cluster ketiga, centroid di (4.5, 8.5)
buat_list(4.5, 8.5)

# simpan dalam bentuk CSV
np.savetxt("cluster.csv", np.column_stack([x_point, y_point]), fmt='%.5f', delimiter=', ')

plt.plot(x_point,y_point, 'x')
plt.show()
