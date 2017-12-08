import os
import struct

import matplotlib.pyplot as plt
import numpy as np
path = os.getcwd() + os.sep + 'MNIST-data' + os.sep
trainimagename = 'train-images-idx3-ubyte'
trainlabelname = 'train-labels-idx1-ubyte'
def readimage(filename, readnumber):
    binfile = open(path + filename , 'rb')
    buf = binfile.read()
    index = 0
    magic, numImages, numRows, numColumns = struct.unpack_from('>IIII', buf, index)
    index += struct.calcsize('>IIII')
    #im = struct.unpack_from('>784B', buf, index)
    #index += struct.calcsize('>784B')
    index += struct.calcsize('>784B') * readnumber
    im = struct.unpack_from('>78400B', buf, index)
    #im = np.array(im)

    writefile = open(path + 'train-images', 'w')
    imlist = []
    for i in im:
        if i > 0:
            imlist.append(255)
        else:
            imlist.append(0)
    #writefile.write(str(imlist))
    """
    im = np.array(imlist)[:784]
    im = im.reshape(28, 28)
    fig = plt.figure()
    plotwindow = fig.add_subplot(111)
    plt.imshow(im, cmap='gray')
    plt.show()
    """
    binfile.close()
    writefile.close()
    return np.array(imlist).reshape(100, 784)
    #for i in imlist:
        #print(i, type(imlist))

def readlabel(filename, readnumber):
    binfile = open(path + os.sep + filename, 'rb')
    buf = binfile.read()
    index = 0
    magic, numImages = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')
    index += struct.calcsize('>B') * readnumber
    im = struct.unpack_from('>100B', buf, index)
    label = np.zeros([100, 10])
    for i in range(100):
        label[i, im[i]] = 1
    #for i in range(10):
    #    print(label[:, i])
    return label
    #
def readtrainimage(number):
    return readimage(trainimagename, number)
def readtrainlabel(number):
    return readlabel(trainlabelname, number)
#a = readtrainimage(trainimagename, 200)
#b = readtrainlabel(trainlabelname, 200)