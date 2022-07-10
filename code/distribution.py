# import packages

# import opencv api for computer vision field
# import numeric api
# import plotting package
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# import system package for argument passing
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # get the file path
        filename = str(sys.argv[1])
    else:
        # print the error messege
        print("you should add something after distribution.py to processing!")
        exit()
    try:
        # load the image with channel BGR
        I = cv.imread(filename, 0) 
        
        # check image color channel
        if len(I.shape) >= 3:
            channel_num = I.shape[-1]
        else:
            channel_num = 1

        # plot the image histogram
        for i in range(channel_num):
            hist = cv.calcHist([I], [i], None, [256], [0, 256])
            plt.plot(hist)
            plt.xlim(0, 257)
            plt.show()
               
    except Exception as ex:
        # print the error messege
        print(ex)
        # print('There is no {} file existing'.format(filename))