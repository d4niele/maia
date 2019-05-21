import numpy as np
from matplotlib import pyplot as plt
N = 10
xs = np.random.random(N)
ys = np.random.random(N)
trend = np.polyfit(xs,ys,1)
plt.plot(xs,ys,'o')
trendpoly = np.poly1d(trend) 
plt.plot(xs,trendpoly(xs))