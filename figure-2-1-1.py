# Section 2.1
# Figure 1
# Modified by Ryan Dorson

from matplotlib.font_manager import FontProperties
from numpy import *
from pylab import *

# Define vectors and scalars
x = array([1, 2])
y = array([2, 1])
z = x + y
half_x = 0.5 * x
two_x = 2 * x

# Plot vectors
fig = figure(figsize=(20, 8))
suptitle('Simple Vector Operations')
prop = FontProperties()
prop.set_file('STIXMath-Regular.otf')

subplot(1, 2, 1)
quiver((0, 0, 0), (0, 0, 0), (two_x[0], x[0], half_x[0]), (two_x[1], x[1], half_x[1]), angles='xy', scale_units='xy', scale=1, color=('purple', 'r', 'b'))
labels = [u'2x = \u27E82, 4\u27E9', u'x = \u27E81, 2\u27E9', u'0.5x = \u27E80.5, 1\u27E9']
xs = [two_x[0], x[0], half_x[0]]
ys = [two_x[1], x[1], half_x[1]]
for label, u, v in zip(labels, xs, ys):
	annotate(label, xy = (u + 0.05, v), fontproperties=prop)
title('Scalar Product')
xlim([0, 5])
ylim([0, 5])
draw()

subplot(1, 2, 2)
plot((x[0], z[0]), (x[1], z[1]), '--r')
plot((y[0], z[0]), (y[1], z[1]), '--b')
quiver((0, 0, 0), (0, 0, 0), (x[0], y[0], z[0]), (x[1], y[1], z[1]), angles='xy', scale_units='xy', scale=1, color=('b', 'r', 'purple'))
labels = [u'x = \u27E81, 2\u27E9', u'y = \u27E82, 1\u27E9', u'x + y = \u27E83, 3\u27E9']
xs = [x[0], y[0], z[0]]
ys = [x[1], y[1], z[1]]
for label, u, v in zip(labels, xs, ys):
	annotate(label, xy = (u + 0.05, v), fontproperties=prop)
title('Vector Addition')
xlim([0, 5])
ylim([0, 5])
draw()

# show()
savefig('figure-2-1-1.png', bbox_inches='tight')
