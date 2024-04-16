#点位图
import numpy as np
import cv2
import random

#设置画布的宽度和高度
width = 600
height = 600
canvas_white = np.ones((height, width, 3), dtype="uint8")
canvas_white *= 255

#起点随机
#a = random.randint(0, width-1)
#b = random.randint(0, height-1)
#固定起点
a = 300
b = 300

#设置接近边界时折返，约定移动10000次
for i in range(0, 10000):
    if a > width - 2:
        c = -1
    elif a < 2:
        c = 1
    else:
        c = random.randint(-1, 1)
    if b > height - 2:
        d = -1
    elif b < 2:
        d = 1
    else:
        d = random.randint(-1, 1)
    x = a + c
    y = b + d
    #路过的点涂成蓝色
    canvas_white[y, x] = [255, 0, 0]
    a = x
    b = y

cv2.imshow("image", canvas_white)
cv2.waitKey(0)
cv2.destroyAllWindows()