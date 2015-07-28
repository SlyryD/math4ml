# Section 1.1
# Figure 1
# Stolen from SciPy.org
# Modified by Ryan Dorson

from scipy import linspace, polyval, polyfit, sqrt, stats, randn
from pylab import plot, title, show, legend, savefig

# Sample data creation
# Number of points 
n = 100
t = linspace(-5, 5, n)
# Parameters
a = 0.8
b = -4
x = polyval([a, b], t)
# Add some noise
xn = x + randn(n)

# Linear regressison -polyfit - polyfit can be used other orders polys
(ar, br) = polyfit(t, xn, 1)
xr = polyval([ar, br], t)
# Compute the mean square error
err = sqrt(sum((xr - xn)**2)/n)

print('Linear regression using polyfit')
print('Parameters: a=%.2f b=%.2f \nRegression: a=%.2f b=%.2f, ms error= %.3f' % (a, b, ar, br, err))

# matplotlib ploting
title('Linear Regression Example')
plot(t, xn, 'bo')
plot(t, xr, 'r--')
legend(['Bunch of points', 'Regression line'], loc=2)
#~ show()

# Linear regression using stats.linregress
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
print('Linear regression using stats.linregress')
print('Parameters: a=%.2f b=%.2f \nRegression: a=%.2f b=%.2f, std error= %.3f' % (a, b, a_s, b_s, stderr))

savefig('figure-1-1-1.png', bbox_inches='tight')
