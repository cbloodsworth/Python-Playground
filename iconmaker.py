import random
import matplotlib.pyplot as plt
import numpy as np

SIZE = 5

# We don't want even-numbered sizes
if SIZE % 2 == 0: SIZE += 1

pixelmap = []
color = np.array([random.randint(0,255),random.randint(0,255),random.randint(0,255)])

for i in range(SIZE):
    pixelmap.append([])
    for j in range(SIZE//2 + 1):
        pixelmap[i].append(color * random.randint(0,1))

    for j in range(SIZE//2-1,-1,-1):
        pixelmap[i].append(pixelmap[i][j])
        



plt.figure()
plt.imshow(pixelmap)
plt.show()
