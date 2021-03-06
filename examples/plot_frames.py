"""
======
Frames
======

In this example, we will demonstrate how to use the TransformManager.
We will add several transforms to the manager and plot all frames in
two reference frames ('world' and 'A').
"""
print(__doc__)


import numpy as np
import matplotlib.pyplot as plt
from pytransform3d.plot_utils import make_3d_axis
from pytransform3d.transformations import random_transform
from pytransform3d.transform_manager import TransformManager


random_state = np.random.RandomState(0)
A2world = random_transform(random_state)
B2world = random_transform(random_state)
A2C = random_transform(random_state)
D2B = random_transform(random_state)

tm = TransformManager()
tm.add_transform("A", "world", A2world)
tm.add_transform("B", "world", B2world)
tm.add_transform("A", "C", A2C)
tm.add_transform("D", "B", D2B)

plt.figure(figsize=(10, 5))

ax = make_3d_axis(3, 121)
ax = tm.plot_frames_in("world", ax=ax, alpha=0.6)
ax.view_init(30, 20)

ax = make_3d_axis(3, 122)
ax = tm.plot_frames_in("A", ax=ax, alpha=0.6)
ax.view_init(30, 20)

plt.show()
