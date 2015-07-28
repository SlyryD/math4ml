# Section 1.1
# Figure 2
# Stolen from Glowing Python
# Modified by Ryan Dorson

from numpy import sin, linspace, power
from pylab import plot, title, show, legend, savefig

def f(x): # sample function
 return x*sin(power(x, 2))

# evaluation of the function
x = linspace(-2, 4, 150)
y = f(x)

a = 1.4
h = 0.1
fprime = (f(a + h) - f(a))/h # derivative
tan = f(a) + fprime*(x - a)  # tangent

# plot of the function and the tangent
title('Derivative Example')
plot(x, y, 'b')
plot(x, tan, '--r')
legend(['Function', 'Tangent line'], loc=2)
plot(a, f(a), 'om')
#~ show()

savefig('figure-1-1-2.png', bbox_inches='tight')
