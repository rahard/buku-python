#read CSV of data and calculate a and b
# y = ax + b
import numpy as np
# do not forget to install scipy first: python3 -m pip install scipy
from scipy import stats

my_csv = np.genfromtxt('linear-regression.csv', delimiter=',')
xp, yp = my_csv.transpose()
gradient,intercept,r_value,p_value,std_err=stats.linregress(xp,yp)
print("Gradient and intercept",gradient,intercept)
print("R-squared",r_value**2)
print("p-value",p_value)
