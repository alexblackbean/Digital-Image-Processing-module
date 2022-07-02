# Import package

# import opencv api for computer vision field
import cv2 as cv
# import system package for argument passing
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        # get the file path
        filename = str(sys.argv[1]) 
    else:
        # print the error messege
        print("you should add something after load_image.py to load image!")    
        exit()
    try:
        # load the image with channel BGR
        I = cv.imread(filename)

        # print the image information
        print("width: {}, height: {}, # of channel: {}".format(I.shape[1], I.shape[0], I.shape[2]))

        # show the image in 5 secs
        cv.imshow('test', I)
        cv.waitKey(5000)
        cv.destroyWindow('test')
    except:
        # print the error messege
        print("There is no {} file existing".format(filename))
    del I
    exit()