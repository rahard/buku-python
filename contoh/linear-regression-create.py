import numpy as np

# persamaan y = a*x + b
a = -0.3
b = 0.87
jumlah_titik = 300

# buat dua list yang masih kosong
x_point = []
y_point = []

for i in range(jumlah_titik):
    x = np.random.normal(0.0,0.4)
    y = a*x + b + np.random.normal(0.0,0.07)
    x_point.append([x])
    y_point.append([y])

np.savetxt("linear-regression-pr.csv", np.column_stack([x_point, y_point]), fmt='%.5f', delimiter=', ')
