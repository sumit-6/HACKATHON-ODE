import numpy as np
from matplotlib import pyplot as plt

#plt.xkcd()

# Differential equation of a pendulum (NON IDEAL CASE)
# a(y_double_dot) = b(y_dot) + c(y)
print('\n')
print("a(d\u00b2y/dx\u00b2) = b(dy/dx) + c(y)")
print('\n')
a = float(input("Enter coffecient of d\u00b2y/dx\u00b2 that is a:"))
b = float(input("Enter coffecient of dy/dx that is b:"))
c = float(input("Enter coffecient of y that is c:"))
y_0 = float(input("Enter initial value of y:"))
y_dot_0 = float(input("Enter initial value of dy/dx:"))
delta_x = 0.01
low_x = float(input("Enter lower limit of x:"))
up_x = float(input("Enter upper limit of x:"))
def get_y_double_dot(y,y_dot):
    return (b/a)*y_dot + (c/a)*y

def y_call(x):
    y=y_0
    y_dot=y_dot_0
    for x_coordinate in np.arange(low_x,x,delta_x):
        y_double_dot=get_y_double_dot(y,y_dot)
        y+=y_dot*delta_x
        y_dot+=y_double_dot*delta_x
    return y,y_dot
y_array = []
y_dot_array = []
for x_coordinate in np.arange(low_x,up_x,delta_x):
    y_array.append(x_coordinate)
    y_dot_array.append(y_call(x_coordinate)[1])
plt.plot(y_array,y_dot_array)
plt.show()
