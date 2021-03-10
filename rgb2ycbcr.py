import cv2
import numpy as np
#2 = red
#1 = green
#0 = blue
def rgb2ycrbr(image):
    img = (image.astype(float))
    YCbCr_img = np.empty((img.shape[0], img.shape[1], 3), float)
    Y = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Cb = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Cr = np.empty([img.shape[0],img.shape[1]], dtype = float)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            Y[i,j] = 0 + (0.299)*(img[i,j][2]) + (0.587)*(img[i,j][1]) + (0.114)*(img[i,j][0])
            Cb[i,j] = 128 - (0.168736)*(img[i,j][2]) - (0.331264)*(img[i,j][1]) + (0.5)*(img[i,j][0])
            Cr[i,j] = 128 + (0.5)*(img[i,j][2]) - (0.418688)*(img[i,j][1]) - (0.081312)*(img[i,j][0])
    #junta as componentes da imagem
    YCbCr_img[:,:,1] = Y
    cv2.imwrite('out_img/Y.bmp', Y)
    YCbCr_img[:,:,0] = Cb
    cv2.imwrite('out_img/Cb.bmp', Cb)
    YCbCr_img[:,:,2] = Cr
    cv2.imwrite('out_img/Cr.bmp', Cr)
    #print(YCbCr_img)
    return YCbCr_img

input_image = cv2.imread('in_img/1024x768.bmp', 1)
#print (input_image)
ycrbr = rgb2ycrbr(input_image)

cv2.imwrite('out_img/ycbcr.bmp', ycrbr)
#cv2.imshow('image',ycrbr)
#cv2.waitKey(0)
#cv2.destroyAllWindows()