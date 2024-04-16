#全图随机颜色
import numpy as np
import cv2
import random

#设置画布的宽度和高度
width = 200
height = 200
canvas_white = np.ones((height, width, 3), dtype="uint8")
canvas_white *= 255

# 设置像素颜色
for i in range(0, height):
    for j in range(0, width):
        #全随机
        #red = random.randint(0, 255)
        #green = random.randint(0, 255)
        #blue = random.randint(0, 255)
        #array_bgr = np.array([blue, green, red])
        #只保留黑和白，黑的概率为0.005
        bgr =np.random.choice([0,1], 1, replace=True, p=[0.005,0.995]  )
        if bgr == 0:
            array_bgr = np.array([0, 0, 0])
            canvas_white[i, j] = array_bgr
        else:
            array_bgr = np.array([255, 255, 255])
        #canvas_white[i, j] = array_bgr

cv2.imshow("image", canvas_white)
cv2.waitKey(0)
cv2.destroyAllWindows()