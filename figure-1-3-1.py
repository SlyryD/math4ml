# Section 1.3
# Figure 1
# Stolen from Glowing Python
# Modified by Ryan Dorson

from numpy import *
from pylab import *

def f(x): # sample function
    return x**4 + x**3 - 4*x*x
 
def fprime(a):
    h = 0.00001
    return (f(a + h) - f(a)) / h

def tanline(a):
    return f(a) + fprime(a)*(x - a)

# evaluation of the function
x = linspace(-3, 3, 198)
y = f(x)

a1 = 0.0
tan1 = tanline(a1)  # tangent line

a2 = (-3 - sqrt(137)) / 8
tan2 = tanline(a2)  # tangent line

a3 = (-3 + sqrt(137)) / 8
tan3 = tanline(a3)  # tangent line

# plot of the function and the tangent lines
title('Non-convex function example')
plot(x, y, 'b')
plot(x, tan1, '--r')
plot(x, tan2, '--g')
plot(x, tan3, '--k')
legend(['Function', 'Local max at x = {:.5}'.format(a1), 'Local min at x = {:.5}'.format(a2), 'Local min at x = {:.5}'.format(a3)], loc=2)
plot(a1, f(a1), 'om')
plot(a2, f(a2), 'om')
plot(a3, f(a3), 'om')
ylim([-20, 20]) 
#~ show()

savefig('figure-1-3-1.png', bbox_inches='tight')
