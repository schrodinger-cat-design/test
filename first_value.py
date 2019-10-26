def f_2d(x,y):
    return x ** 2 + 3 * x + y ** 2 + 8 * y + 1
def df_2d(x,y):
    return 2 * x + 3, 2 * y + 8
x , y = 4, 2
for itr in range(50):
    v_x,v_y = df_2d(x,y)
    x,y =x - 0.1 * v_x,y - 0.1 * v_y
    print("f({},{})={}".format(x,y,f_2d(x,y)))

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-6,3)
y = np.linspace(-8,2)
X, Y = np.meshgrid(x,y)
fig = plt.figure()
ax = fig.gca(projection = '3d')
surf = ax.plot_surface(X,Y,f_2d(X,Y))
plt.show()