# -*- coding: utf-8 -*-
import os
import cv2
import time
import threading
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
os.system('')  # 在cmd窗口显示颜色模式

# 显示或保存图片
def cv_show(name, img, save=True):  # 任意地方调用保存处理过的背景图或滑块图，默认保存画框背景图
    path = r'show_img/'
    if save:
        cv2.imwrite(path + name + '.png', img)
    else:
        pass
    cv2.imshow(name, img)

# 异常输出检查
def except_output():
    # msg用于自定义函数的提示
    def except_execute(func):
        @wraps(func)
        def except_print(*args, **kwargs):
            try:
                _start_time = time.perf_counter()
                res = func(*args, **kwargs)
                return res
            except TimeoutError as t:
                print("超时: " + str(t))
            except Exception as e:
                print("函数错误: " + str(e))
        return except_print
    return except_execute


# 单例元类
class SingleType(type):
    _instance = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            with SingleType._lock:
                if not cls._instance:
                    cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


# 演示
class MySlider(metaclass=SingleType):
    # _instance = None

    # 获取大小
    @except_output()  # 滑块异常
    def fix_img(self, filename):
        # 图像处理
        img = cv2.imread(filename)  # 读取图像：imread 默认的 BGR 色彩。默认加载彩色图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        cv2.imshow(f"fix_img-imread-{filename}", img)  # 显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度处理：BGR→灰度转换，我们使用标志cv.COLOR_BGR2GRAY。http://www.woshicver.com/FifthSection/4_1_%E6%94%B9%E5%8F%98%E9%A2%9C%E8%89%B2%E7%A9%BA%E9%97%B4/
        cv2.imshow(f"fix_img-cvtColor-{filename}", gray)  # 显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        ret, thresh = cv2.threshold(gray, 125, 200, cv2.THRESH_BINARY) # 图像阈值。http://www.woshicver.com/FifthSection/4_3_%E5%9B%BE%E5%83%8F%E9%98%88%E5%80%BC/#_3
        cv2.imshow(f"fix_img-threshold-{filename}", thresh)  # 显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/

        # 轮廓处理
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 查找轮廓：为了获得更高的准确性，请使用二进制图像。因此，在找到轮廓之前，请应用阈值或canny边缘检测。http://www.woshicver.com/FifthSection/4_9_1_OpenCV%E4%B8%AD%E7%9A%84%E8%BD%AE%E5%BB%93/#_3
        # cv2.imshow(f"fix_img-查找轮廓:findContours-{filename}", contours)  # 注意：不可用于显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        contour_img = cv2.drawContours(img, contours, 0, (0, 255, 0), 3)  # 绘制轮廓：http://www.woshicver.com/FifthSection/4_9_1_OpenCV%E4%B8%AD%E7%9A%84%E8%BD%AE%E5%BB%93/#_4
        cv2.imshow(f"fix_img-drawContours-{filename}", contour_img)  # 显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        x, y, w, h = cv2.boundingRect(contours[0])  # 轮廓特征：边界矩形>直角矩形 (x，y)为矩形的左上角坐标，而(w，h)为矩形的宽度和高度.http://www.woshicver.com/FifthSection/4_9_2_%E8%BD%AE%E5%BB%93%E7%89%B9%E5%BE%81/#7
        mixintu = contour_img[y:y + h, x:x + w]
        cv2.imshow(f"fix_img-boundingRect-{filename}", mixintu)  # 显示图像。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        return mixintu

    @except_output()  # 匹配异常
    def run(self, name, images):
        # 第一步，对滑块进行图片处理
        tp_img = self.fix_img(images[0])  # 裁掉透明部分找出滑块大小
        tp_edge = cv2.Canny(tp_img, 100, 200)  # Canny边缘检测：http://www.woshicver.com/FifthSection/4_7_Canny%E8%BE%B9%E7%BC%98%E6%A3%80%E6%B5%8B/
        tp_pic = cv2.cvtColor(tp_edge, cv2.COLOR_GRAY2BGR)  # 彩色处理：灰度转换→BGR，我们使用标志cv.COLOR_BGR2GRAY。http://www.woshicver.com/FifthSection/4_1_%E6%94%B9%E5%8F%98%E9%A2%9C%E8%89%B2%E7%A9%BA%E9%97%B4/
        cv_show(f"run-cvtColor-images[0]-{name}", tp_pic)  # 保存裁掉透明滑块的处理图

        # 第二步，对背景图片进行处理
        bg_img = cv2.imread(images[1], -1)  # 读取图像：imread 默认的 BGR 色彩。加载图像，包括alpha通道。http://www.woshicver.com/ThirdSection/2_1_%E5%9B%BE%E5%83%8F%E5%85%A5%E9%97%A8/
        bg_edge = cv2.Canny(bg_img, 100, 200)  # Canny边缘检测：http://www.woshicver.com/FifthSection/4_7_Canny%E8%BE%B9%E7%BC%98%E6%A3%80%E6%B5%8B/
        bg_pic = cv2.cvtColor(bg_edge, cv2.COLOR_GRAY2BGR)  # 彩色处理：灰度转换→BGR，我们使用标志cv.COLOR_BGR2GRAY。http://www.woshicver.com/FifthSection/4_1_%E6%94%B9%E5%8F%98%E9%A2%9C%E8%89%B2%E7%A9%BA%E9%97%B4/
        cv_show(f"run-cvtColor-images[1]-{name}", bg_pic)

        # 第三步， 使用相关系数匹配和归一化相关系数匹配
        methods = [cv2.TM_CCORR]
        # methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF,
        #            cv2.TM_CCOEFF_NORMED]
        results = {}
        move = 0
        for meth in methods:
            tem_full_img = bg_pic.copy()
            res = cv2.matchTemplate(tem_full_img, tp_pic, meth)
            loc = cv2.minMaxLoc(res)[3]
            results[meth] = loc  # test
            move = loc[0]

            # 绘制框
            th, tw = tp_pic.shape[:2]
            bottom_right = (loc[0] + tw, loc[1] + th)
            cv2.rectangle(bg_img, loc, bottom_right, (0, 225, 0), 2)
            cv_show(f'{name}', bg_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return move


def crawler(my_slider, name, images):
    return my_slider.run(name, images)  # 距离

# 启用线程池执行，提高效率
def start_main_by_thread_pool():
    start_time = time.perf_counter()
    print('开始')
    pool = ThreadPoolExecutor(max_workers=3, thread_name_prefix='thread')  # 多线程匹配
    params = {
        '1': ('./demo_img/pt11.png', './demo_img/pt1.png'),
        '2': ('./demo_img/pt22.png', './demo_img/pt2.png'),
        '3': ('./demo_img/pt33.png', './demo_img/pt3.png')
    }
    for i, images in params.items():
        my_slider = MySlider()
        move = pool.submit(crawler, my_slider, f"task-{i}", images).result()
        print(images[1], "最大移动距离", move)
    pool.shutdown()
    print('结束总运行时长：%f秒' % (time.perf_counter() - start_time))

# 顺序执行
def start_main():
    start_time = time.perf_counter()
    print('开始')
    params = {
        '1': ('./demo_img/pt11.png', './demo_img/pt1.png'),
        # '2': ('./demo_img/pt22.png', './demo_img/pt2.png'),
        # '3': ('./demo_img/pt33.png', './demo_img/pt3.png')
    }
    for i, images in params.items():
        my_slider = MySlider()
        move = my_slider.run(f"task-{i}", images)
        print(images[1], "最大移动距离", move)

        cv2.waitKey()
        cv2.destroyAllWindows()
    print('结束总运行时长：%f秒' % (time.perf_counter() - start_time))

if __name__ == '__main__':
    # 顺序执行
    start_main()

    # 启用线程池执行，提高效率
    #   - macOS 会报错：`WARNING: nextEventMatchingMask should only be called from the Main Thread`。请使用 `start_main()` 方法
    # start_main_by_thread_pool()
