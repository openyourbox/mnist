import draw
import numpy as np
import matplotlib.pyplot as plt
draw.draw()
mmp = []
print(mmp)
im = open('draw.txt').readlines()
print(im)
im = [i.strip() for i in im]
print(len(im))
print(im)
for i in im:
    mmp.append(int(i))
print(mmp)
print(type(mmp[3]))
image = np.zeros((28, 28))
for i in range(28):
    for j in range(28):
        image[i, j] = mmp[i * 28 + j]
#image = image / 255
#image.reshape((28, 28))
print(image)

def plot(im):
    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im, cmap='gray')
    plt.show()
#plot(image)