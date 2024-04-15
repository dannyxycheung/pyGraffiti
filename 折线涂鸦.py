import numpy as np
import cv2
import random

#设置画布的宽度和高度
width = 800
height = 600
#设置每一笔的相对宽度和高度最大值
width_step_max = 15
height_step_max = 15
canvas_white = np.ones((height, width, 3), dtype="uint8")
canvas_white *= 255

#随机生成开始的xy坐标
x = random.randint(0, width)
y = random.randint(0, height)

array_ori_x = np.array([x])
array_ori_y = np.array([y])

#随机生成每一笔的增量xy坐标数组
random_x = np.random.randint(1, width_step_max, size=100)
random_y = np.random.randint(1, height_step_max, size=100)
#纵坐标增量的偶数行设置为负
even_random_y = random_y[::2]
even_random_y *= -1

#原点坐标和增量坐标合并成一个数组
array_step_x = np.concatenate((array_ori_x, random_x))
array_step_y = np.concatenate((array_ori_y, random_y))
array_sum_x = np.cumsum(array_step_x)
array_sum_y = np.cumsum(array_step_y)

random_xy = np.column_stack((array_sum_x, array_sum_y))

cv2.polylines(canvas_white, [random_xy], False, (255,0,0))

cv2.imshow("image", canvas_white)
cv2.waitKey(0)
cv2.destroyAllWindows()