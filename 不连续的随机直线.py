import numpy as np
import cv2
import random

#设置画布的宽度和高度
width = 800
height = 600
canvas_white = np.ones((height, width, 3), dtype="uint8")
canvas_white *= 255

#循环的次数就是画线的数量
for i in range(0, 100):
    x = random.randint(0, width)
    y = random.randint(0, height)
    a = random.randint(0, width)
    b = random.randint(0, height)
#画直线
    cv2.line(canvas_white,(x,y),(a,b),(255,0,0),1)

cv2.imshow("image", canvas_white)
cv2.waitKey(0)
cv2.destroyAllWindows()