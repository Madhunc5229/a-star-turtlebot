import numpy as np
import cv2





scale = 100
gmap = np.ones((1*scale, 4*scale, 3), dtype="uint8")

c = 9
# c =0
for y in range(100):
    for x in range(400):
        #Square_1
        sq_1_1 = y - 0.575 * scale - c
        sq_1_2 = x - 1.425 *scale +c
        sq_1_3 = y - 0.425 * scale +c
        sq_1_4 = x - 1.575 *scale -c

        #Square_2
        sq_2_1 = y - 0.8 * scale - c
        sq_2_2 = x - 1.925 * scale +c
        sq_2_3 = y - 0.65 * scale + c
        sq_2_4 = x - 2.075 *scale - c

        #Square_3
        sq_3_1 = y - 0.35 * scale - c
        sq_3_2 = x - 1.925 *scale +c
        sq_3_3 = y - 0.2 * scale +c
        sq_3_4 = x - 2.075 *scale-c


        #Square_4
        sq_4_1 = y - 0.575 * scale - c
        sq_4_2 = x - 2.425 *scale + c
        sq_4_3 = y - 0.425 * scale + c
        sq_4_4 = x - 2.575 *scale -c
        if (sq_1_1<0 and sq_1_2>0 and sq_1_3>0 and sq_1_4<0) or (sq_2_1<0 and sq_2_2>0 and sq_2_3>0 and sq_2_4<0) or (sq_3_1<0 and sq_3_2>0 and sq_3_3>0 and sq_3_4<0) or (sq_4_1<0 and sq_4_2>0 and sq_4_3>0 and sq_4_4<0 ):
            gmap[99-y, x, 0] = 255
        

# cv2.imshow("Map", gmap)
# cv2.waitKey(0)

'''
for x in range(1*scale):
    for y in range(4*scale):

        x = (1*scale - 1) - x

        #Square_1
        sq_1_1 = x - 0.575 * scale - c
        sq_1_2 = y - 1.425 *scale +c
        sq_1_3 = x - 0.425 * scale +c
        sq_1_4 = y - 1.575 *scale -c

        #Square_2
        sq_2_1 = x - 0.8 * scale - c
        sq_2_2 = y - 1.925 * scale +c
        sq_2_3 = x - 0.65 * scale + c
        sq_2_4 = y - 2.075 *scale - c

        #Square_3
        sq_3_1 = x - 0.35 * scale - c
        sq_3_2 = y - 1.925 *scale +c
        sq_3_3 = x - 0.2 * scale +c
        sq_3_4 = y - 2.075 *scale-c


        #Square_4
        sq_4_1 = x - 0.575 * scale - c
        sq_4_2 = y - 2.425 *scale + c
        sq_4_3 = x - 0.425 * scale + c
        sq_4_4 = y - 2.575 *scale -c
        if (sq_1_1<0 and sq_1_2>0 and sq_1_3>0 and sq_1_4<0) or (sq_2_1<0 and sq_2_2>0 and sq_2_3>0 and sq_2_4<0) or (sq_3_1<0 and sq_3_2>0 and sq_3_3>0 and sq_3_4<0) or (sq_4_1<0 and sq_4_2>0 and sq_4_3>0 and sq_4_4<0 ):
            gmap[x, y, 0] = 255
'''




