# Section 2.1
# Figure 1
# Modified by Ryan Dorson

from matplotlib.font_manager import FontProperties
from numpy import *
from pylab import *

# Define vectors and scalars
c = 2
x = array([1, 2])
y = array([2, 1])
z = x + y
cx = c * x

# Plot vectors
fig = figure(figsize=(20, 8))
suptitle('Simple Vector Operations')
prop = FontProperties()
prop.set_file('STIXMath-Regular.otf')

subplot(1, 2, 1)
plot((x[0], z[0]), (x[1], z[1]), '--r')
plot((y[0], z[0]), (y[1], z[1]), '--b')
quiver((0, 0, 0), (0, 0, 0), (x[0], y[0], z[0]), (x[1], y[1], z[1]), angles='xy', scale_units='xy', scale=1, color=('b', 'r', 'purple'))
labels = [u'x = \u27E81, 2\u27E9', u'y = \u27E82, 1\u27E9', u'x + y = \u27E83, 3\u27E9']
xs = [x[0], y[0], z[0]]
ys = [x[1], y[1], z[1]]
for label, u, v in zip(labels, xs, ys):
	annotate(label, xy = (u, v), fontproperties=prop)
title('Vector Addition')
xlim([0, 5])
ylim([0, 5])
draw()

subplot(1, 2, 2)
quiver((0, 0), (0, 0), (cx[0], x[0]), (cx[1], x[1]), angles='xy', scale_units='xy', scale=1, color=('r', 'b'))
labels = [u'x = \u27E81, 2\u27E9', u'2x = \u27E82, 4\u27E9']
xs = [x[0], cx[0]]
ys = [x[1], cx[1]]
for label, u, v in zip(labels, xs, ys):
	annotate(label, xy = (u, v), fontproperties=prop)
title('Scalar Product')
xlim([0, 5])
ylim([0, 5])
draw()

# show()
savefig('figure-2-1-1.png', bbox_inches='tight')
