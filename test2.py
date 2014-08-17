import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x=np.arange(0,5,.01)
fig, ax = plt.subplots()
for i in range(10):
    y = [np.sin(datum**2+i/10.0) for datum in x]
    ax.plot(x, y)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_title("The new color cycle is a little prettier by default", y=1.05)
ax.set_ylabel(r"$sin(x^{2}+\lambda{})$", labelpad=5)
ax.set_xlabel(r"x", labelpad=5)
plt.savefig('test2.png')
plt.show()