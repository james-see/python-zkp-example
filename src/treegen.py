import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib import colors as mcolors


width_dist = 10
depth_dist = 10
levels = 5

def bintree_level(levels, x, y, width):
    segments = []
    xl = x + depth_dist
    yl = y - width / 2
    xr = x + depth_dist
    yr = y + width / 2
    segments.append([[x, y], [xl, yl]])
    segments.append([[x, y], [xr, yr]])
    if levels > 1:
        segments += bintree_level(levels - 1, xl, yl, width / 2)
        segments += bintree_level(levels - 1, xr, yr, width  / 2)
    return segments

segs = bintree_level(levels, 0, 0, width_dist)

colors = [mcolors.to_rgba(c)
          for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]
line_segments = LineCollection(segs, linewidths=1, colors=colors, linestyle='solid')

fig, ax = plt.subplots()
ax.set_xlim(-1, levels * depth_dist + 1)
ax.set_ylim(-1.5*width_dist, 1.5*width_dist)
ax.add_collection(line_segments)
plt.show()