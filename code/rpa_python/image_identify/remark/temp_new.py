# -*- coding: utf-8 -*-
import cv2
import numpy as np


# 相关系数相似匹配，找出坐标最大值，并返回最大横坐标
def template_match(bg_image, fg_image):
    res = cv2.matchTemplate(bg_image, fg_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    return [min_val, max_val, min_loc, max_loc]


# 图像边缘检测
def sobel_edge(image):
    image_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    abs_x = cv2.convertScaleAbs(image_x)

    image_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    abs_y = cv2.convertScaleAbs(image_y)
    
    dst = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return np.asarray(dst, dtype=np.uint8)


# 最小区域的矩形计算
def edge(img):
    np_data = np.array(img)
    rr = np.where(np_data != 0)
    x_min = min(rr[1])
    y_min = min(rr[0])
    x_max = max(rr[1])
    y_max = max(rr[0])
    return x_min, y_min, x_max, y_max


# 读取下载好的文件进行灰度处理，之后进行高斯模糊平滑图像，最终返回边缘检测结果
def read(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # image = cv2.GaussianBlur(image, (1, 1), 0)
    # 
    cv2.imshow("img_window", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sobel_edge(image)


# 测试结果
def draw_line(p1, p2, value):
    image1 = cv2.imread(p1, 1)
    image2 = cv2.imread(p2, 1)
    h, w = image2.shape[:2]  # rows->h, cols->w
    # print('高：', h, "宽：", w)
    left_top = value[3]  # 左上角
    right_bottom = (left_top[0] + w, left_top[1] + h)  # 右下角
    cv2.rectangle(image1, left_top, right_bottom, (0, 0, 255), 2)  # 画出矩形位置

    # 显示图片，参数：（窗口标识字符串，imread读入的图像）
    cv2.imshow("img_window", image1)
    # 窗口等待任意键盘按键输入,0为一直等待,其他数字为毫秒数
    cv2.waitKey(0)
    # 销毁窗口，退出程序
    cv2.destroyAllWindows()


if __name__ == '__main__':
    path_1 = 'canvas.png'
    path_2 = 'blockHead.png'

    fg_image = read(path_1)
    bg_image = read(path_2)

    x_min, y_min, x_max, y_max = edge(fg_image)

    fg_image = fg_image[y_min:y_max, :]
    bg_image = bg_image[y_min:y_max, :]
    values = template_match(bg_image, fg_image)

    # print(values)
    draw_line(path_1, path_2, values)
