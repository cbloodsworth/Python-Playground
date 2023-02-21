import random
import matplotlib.pyplot as plt
import numpy as np

pixelmap = []
color = np.array([random.randint(0,255),random.randint(0,255),random.randint(0,255)])

for i in range(5):
    pixelmap.append([])
    for j in range(3):
        pixelmap[i].append(color * random.randint(0,1))
        

for i in range(5):
    for j in range(1,-1,-1):
        pixelmap[i].append(pixelmap[i][j])


plt.figure()
plt.imshow(pixelmap)
plt.show()
