#一笔连续涂鸦
import numpy as np
import cv2

#设置画布的宽度和高度
width = 800
height = 600
canvas_white = np.ones((height, width, 3), dtype="uint8")
canvas_white *= 255

random_x = np.random.randint(0, width, size=101)
random_y = np.random.randint(0, height, size=101)
random_xy = np.column_stack((random_x, random_y))

cv2.polylines(canvas_white, [random_xy], False, (255,0,0))

cv2.imshow("image", canvas_white)
cv2.waitKey(0)
cv2.destroyAllWindows()