from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
#im = np.zeros([28, 28])
def draw():
    root = Tk()
    image = np.zeros([280, 280])
    # 创建一个框架，在这个框架中响应事件
    # frame = Frame(root,width=280, height=280)
    canvas = Canvas(root, width=280, height=280, bg='white')
    canvas.pack()

    def callBack(event):
        try:
            """
            for i in range(40):
                for j in range(40):
                    if(i == 20 and j == 20):
                        image[event.y, event.x] = 255
                    else:
                        image[event.y - 20 + j, event.x - 20 + i] = 255 / np.sqrt((20-j)*(20-j) + (20-i)*(20-i))
            image[event.y - 10:event.y + 10, event.x - 10:event.x + 10] = 255
            """
            image[event.y - 10:event.y + 10, event.x - 10:event.x + 10] = image[event.y - 10:event.y + 10,
                                                                          event.x - 10:event.x + 10] + 30

        except:
            pass
        canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill='black')
        # print("现在的位置是", event.x, event.y)  # 按哪个键，在Shell中打印

    canvas.bind("<B1-Motion>", callBack)
    # frame.bind("<B1-Motion>", callBack)
    # frame.pack()
    small_image = np.zeros([28, 28])



    def displayClear(event):
        image[image > 255] = 255
        for i in range(28):
            for j in range(28):
                temp = image[i * 10: (i + 1) * 10, j * 10: (j + 1) * 10]
                #small_image[i, j] = temp.sum() / temp.size
                small_image[i, j] = temp.sum() / (temp[temp > 0].size if temp[temp > 0].size > 0 else 1)
        """
        fig = plt.figure()
        plotwindow = fig.add_subplot(111)    
        plt.imshow(im, cmap='gray')
        plt.show()    
        # canvas.delete(ALL)
        """
        #im = small_image / small_image.max() * 255
        im = small_image
        print('im.size is :', im.size)
        #im.reshape((1, 784))
        file = open('draw.txt', 'w')
        for i in im:
            for j in i:
                file.write(str(int(j)) + '\n')
                #print(j, end=' ')
            #file.write('\r\n')
            #print('\r\n')
        file.close()

        # canvas.destroy()
        #im = small_image / small_image.max()
        # im = im.reshape((1, 784))
        root.destroy()

    canvas.bind("<Button-3>", displayClear)

    mainloop()