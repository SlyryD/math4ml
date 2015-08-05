# Section 1.1
# Figure 2
# Stolen from Glowing Python
# Modified by Ryan Dorson

from numpy import *
from pylab import *

def f(x): # sample function
    return 2*x*x - 3*x + 1
 
def fprime(a):
    h = 0.00001
    return (f(a + h) - f(a)) / h

def tanline(a):
    return f(a) + fprime(a)*(x - a)

# evaluation of the function
x = linspace(-2, 5, 175)
y = f(x)

a1 = 3.0 / 4
tan1 = tanline(a1)  # tangent line

a2 = 3.0
tan2 = tanline(a2)  # tangent line

# plot of the function and the tangent lines
title('Derivative Example')
plot(x, y, 'b')
plot(x, tan1, '--r')
plot(x, tan2, '--g')
legend(['Function', 'Slope at x = 3/4', 'Slope at x = 3'], loc=2)
plot(a1, f(a1), 'om')
plot(a2, f(a2), 'om')
ylim([-20, 40]) 
#~ show()

savefig('figure-1-1-2.png', bbox_inches='tight')
