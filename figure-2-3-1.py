# Section 2.1
# Figure 1
# Modified by Ryan Dorson

from matplotlib.font_manager import FontProperties
from numpy import *
from pylab import *

# Define vectors and scalars
x = array([3, 1])
y = array([1, 2])

# Plot vectors
fig = figure(figsize=(8, 8))
title('Dot Product - Angle Relationship')
prop = FontProperties()
prop.set_file('STIXMath-Regular.otf')

quiver((0, 0), (0, 0), (y[0], x[0]), (y[1], x[1]), angles='xy', scale_units='xy', scale=1, color=('r', 'b'))
plot((y[0], 1.5), (y[1], 0.5), '--m')
labels = ['y', 'x']
xs = [y[0], x[0]]
ys = [y[1], x[1]]
for label, u, v in zip(labels, xs, ys):
	annotate(label, xy=(u + 0.05, v), fontproperties=prop)
annotate(u"\u03D1", xy=(0.125, 0.1), fontproperties=prop)
axis([0, 3.5, 0, 3.5])
draw()

# show()
savefig('figure-2-3-1.png', bbox_inches='tight')
