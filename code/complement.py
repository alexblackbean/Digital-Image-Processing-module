# import packages

# import opencv api for computer vision field
# import numeric api
import numpy as np
import cv2 as cv
# import system package for argument passing
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # get the file path
        filename = str(sys.argv[1])
    else:
        # print the error messege
        print("you should add something after complement.py to processing!")
        exit()
    try:
        # load the image with channel BGR
        I = cv.imread(filename)

        # calculate complement
        cm = np.zeros(I.shape, np.uint8) + 255
        c_img = cv.scaleAdd(I, -1, cm)

        # show the image in 10 secs
        cv.imshow('test', c_img)
        cv.waitKey(10000)
        cv.destroyAllWindows()
    except:
        # print the error messege
        print('There is no {} file existing'.format(filename))
    del I
    exit()