import cv2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

hatsune = cv2.imread('./hatsune.png', cv2.IMREAD_UNCHANGED)
hatsune = cv2.cvtColor(hatsune, cv2.COLOR_BGRA2RGBA)

hatsune_one_dim = hatsune.reshape(-1, 4)
hatsune_one_dim = hatsune_one_dim[hatsune_one_dim[:, 3] != 0]
hatsune_one_dim = hatsune_one_dim[:, 0:3]

hatsune_pd = pd.DataFrame(hatsune_one_dim, columns=['Red', 'Green', 'Blue'])
hatsune_pd = hatsune_pd.pivot_table(columns=['Red', 'Green', 'Blue'], aggfunc=np.size).reset_index(name='Size').sort_values('Size', ascending=False)

rgbs = hatsune_pd[['Red', 'Green', 'Blue']].to_numpy(dtype=np.uint8)
ss = hatsune_pd['Size'].to_numpy(dtype=np.uint32)
rs = rgbs[:, 0]
gs = rgbs[:, 1]
bs = rgbs[:, 2]
cs = ['#' + hex((rgb[0] << 16) + (rgb[1] << 8) + rgb[2])[2:].zfill(6) for rgb in rgbs]

fig = plt.figure(figsize=[19.2, 10.8], dpi=96.0)
plt.rcParams['axes.facecolor'] = 'none'

ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')

ax.scatter(rs, gs, bs, c=cs, s=ss, marker='.', depthshade=False)

#plt.savefig('hatsune_plot.png')
plt.show()
