# import packages

# import opencv api for computer vision field
import cv2 as cv
# import opencv MACRO
from cv2 import COLOR_BGR2RGB, COLOR_BGR2HSV, COLOR_BGR2HSV_FULL,\
                 COLOR_BGR2GRAY, COLOR_BGR2LAB, COLOR_BGR2HLS
# import system package
import sys


if __name__ == '__main__':
    # color_space index list
    color_space = ['BGR', 'RGB', 'HSV', 'HSV_FULL', 'GRAY', 'CIELAB', 'HLS']

    # color_space macro list
    color_spaceM = [None, COLOR_BGR2RGB, COLOR_BGR2HSV, COLOR_BGR2HSV_FULL,\
                 COLOR_BGR2GRAY, COLOR_BGR2LAB, COLOR_BGR2HLS]

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

        # resize images to fit window
        I = cv.resize(I, (512, 512))
        
        # for every color_space, produce the corresponding images and show them
        for i, space in enumerate(color_space):
            # BGR (original image)
            if space == 'BGR':
                cv.imshow(space, I)
            else:
                # for other color_space
                temp = cv.cvtColor(I, color_spaceM[i])
                cv.imshow(space, temp)

        # wait for user to press any key to exit
        cv.waitKey(0)

        # destroy all existed windows
        cv.destroyAllWindows()
    except Exception as ex:
        # print the error messege
        print(ex)
        print("There is no {} file existing".format(filename))
    del I
    del temp
