# Section 1.2
# Figure 1
# Stolen from 1-1-2
# Modified by Ryan Dorson

from numpy import *
from pylab import *

def f(x): # sample function
    return -x*x + 4

# evaluation of the function
x = linspace(-2, 2, 128)
y = f(x)

n1 = (1 << 3)
w1 = 4.0 / n1
x1 = linspace(-2, 2, n1 + 1)
y1 = f(x1)
sum1 = w1 * sum(y1)

n2 = (1 << 5)
w2 = 4.0 / n2
x2 = linspace(-2, 2, n2 + 1)
y2 = f(x2)
sum2 = w2 * sum(y2)

# plot of the function and the tangent lines
fig = figure(figsize=(20, 8))
suptitle('Approximate Area Under the Curve')

subplot(1, 2, 1)
plot(x, y, 'b')
bar(x1, y1, width=w1, color='r')
title("{0} Rectangles".format(n1))
text(2.4, 3.900, "Approx sum: {0:.4f}".format(sum1), verticalalignment='top', horizontalalignment='right')
text(2.4, 3.775, "Actual sum:  {0:.4f}".format(32.0 / 3), verticalalignment='top', horizontalalignment='right')

subplot(1, 2, 2)
plot(x, y, 'b')
bar(x2, y2, width=w2, color='r')
title("{0} Rectangles".format(n2))
text(2.4, 3.900, "Approx sum: {0:.4f}".format(sum2), verticalalignment='top', horizontalalignment='right')
text(2.4, 3.775, "Actual sum:  {0:.4f}".format(32.0 / 3), verticalalignment='top', horizontalalignment='right')
#~ show()

savefig('figure-1-2-1.png', bbox_inches='tight')
