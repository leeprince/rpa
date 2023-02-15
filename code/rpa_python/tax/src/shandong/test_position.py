import cv2
import time
import numpy as np
from PIL import Image

from tax.src.shandong.main import Tax


def test_get_position_of_chaojiying():
    taxInstance = Tax("")

    canvasElemImgPath = "image/validate_code/canvasElemImg.png"
    position = taxInstance.get_position_of_chaojiying(canvasElemImgPath)
    if not position:
        print('[] get_position_of_chaojiying failed:not position')
        return
    print("[x] get_position_of_chaojiying success:",
          position,
          position[0],
          position[1])


def test_get_position():
    print()

    # --- 使用包含成功移动信息的测试数据，注释则使用正常流程保存的数据
    canvasElemImgPath = "./typora/validate_code/canvasElemImg.test.png"
    blockElemImgPath = "./typora/validate_code/blockElemImg.test.png"
    # --- 使用包含成功移动信息的测试数据，注释则使用正常流程保存的数据-end

    # 遮罩图
    canvasElemImg = Image.open(canvasElemImgPath)
    # 遮罩图的真实尺寸。0:宽度；1:高度
    canvasElemImgRealWidth = canvasElemImg.size[0]
    # 裁剪图
    blockElemImg = Image.open(blockElemImgPath)
    # 裁剪图的真实尺寸。0:宽度；1:高度
    blockElemImgRealWidth = blockElemImg.size[0]
    print(">>>>>\r\n"
          "\t canvasElemImgRealWidth：%s \r\n"
          "\t blockElemImgRealWidth：%s \r\n"
          % (canvasElemImgRealWidth, blockElemImgRealWidth))

    # --- 查找匹配区域 ---
    # - 1
    position = get_position_test_1(canvasElemImgPath, blockElemImgPath)
    slidIngDragX = position[1]
    print("get_position_test_1>>>>>\r\n"
          "\t position：%s \r\n"
          "\t slidIngDragX：%s \r\n"
          % (position, slidIngDragX))
    if slidIngDragX + 4 > 247 and slidIngDragX - 4 < 247:
        print("--------------->>>>>>> 在范围内")
    else:
        print("---------------<<<<<<< 不在范围内")
    # - 2
    position = get_position_test_2(canvasElemImgPath, blockElemImgPath)
    slidIngDragX = position[1]
    print("get_position_test_2>>>>>\r\n"
          "\t position：%s \r\n"
          "\t slidIngDragX：%s \r\n"
          % (position, slidIngDragX))
    if slidIngDragX + 4 > 247 and slidIngDragX - 4 < 247:
        print("--------------->>>>>>> 在范围内")
    else:
        print("---------------<<<<<<< 不在范围内")
    # --- 查找匹配区域-end ---


def get_position_test_1(canvasElemImgPath, blockElemImgPath):
    """canvasElemImgPath, blockElemImgPath
    判断缺口位置
    :param canvasElemImgPath: 遮罩图的文件路径
    :param blockElemImgPath: 裁剪图的文件路径
    :return: 位置 x, y
    """
    cctime = str(int(time.mktime(time.localtime())))
    canvasElemImgFileName = 'test_img/validate_code/cv.canvasElemImg.' + cctime + ".t1."
    blockElemImgFileName = 'test_img/validate_code/cv.blockElemImg.' + cctime + ".t1."

    canvasElemImg = cv2.imread(canvasElemImgPath, 0)
    cv2.imwrite(canvasElemImgFileName + "01.png", canvasElemImg)
    canvasElemImg = cv2.imread(canvasElemImgFileName + "01.png")
    canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    canvasElemImg = abs(255 - canvasElemImg)
    cv2.imwrite(canvasElemImgFileName + "01.png", canvasElemImg)
    canvasElemImg = cv2.imread(canvasElemImgFileName + "01.png")

    blockElemImg = cv2.imread(blockElemImgPath, 0)
    cv2.imwrite(blockElemImgFileName + "01.png", blockElemImg)
    blockElemImg = cv2.imread(blockElemImgFileName + "01.png")

    result = cv2.matchTemplate(canvasElemImg, blockElemImg, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    return x, y


def get_position_test_2(canvasElemImgPath, blockElemImgPath):
    """canvasElemImgPath, blockElemImgPath
    判断缺口位置
    :param canvasElemImgPath: 遮罩图的文件路径
    :param blockElemImgPath: 裁剪图的文件路径
    :return: 位置 x, y
    """
    cctime = str(int(time.mktime(time.localtime())))
    canvasElemImgFileName = 'test_img/validate_code/cv.canvasElemImg.' + cctime + ".t2."
    blockElemImgFileName = 'test_img/validate_code/cv.blockElemImg.' + cctime + ".t2."

    canvasElemImg = cv2.imread(canvasElemImgPath, -1)
    cv2.imwrite(canvasElemImgFileName + "01.png", canvasElemImg)

    blockElemImg = cv2.imread(blockElemImgPath, 0)
    cv2.imwrite(blockElemImgFileName + "01.png", blockElemImg)
    blockElemImg = cv2.imread(blockElemImgFileName + "01.png")

    result = cv2.matchTemplate(canvasElemImg, blockElemImg, cv2.TM_CCOEFF_NORMED)
    x, y = np.unravel_index(result.argmax(), result.shape)
    return x, y


def test_opencv():
    canvasElemImgPath = "./typora/validate_code/canvasElemImg.test.png"

    cctime = str(int(time.mktime(time.localtime())))
    canvasElemImgFileName = 'test_img/validate_code/cv.canvasElemImg.' + cctime  # .png

    # --- 1
    # canvasElemImg = cv2.imread(canvasElemImgPath, 0)
    # cv2.imshow('canvasElemImg.1.01-01', canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".1.01.png", canvasElemImg)
    #
    # canvasElemImg = cv2.imread(canvasElemImgFileName + ".1.01.png")
    # cv2.imshow('canvasElemImg.1.01-02', canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".1.01.png", canvasElemImg)
    #
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('canvasElemImg.1.01-03', canvasElemImg)
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imshow('canvasElemImg.1.01-04', canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".1.02.png", canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    # --- 2
    # canvasElemImg = cv2.imread(canvasElemImgPath, 1)
    # cv2.imwrite(canvasElemImgFileName + ".2.01.png", canvasElemImg)
    #
    # canvasElemImg = cv2.imread(canvasElemImgFileName + ".01.png")
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".2.02.png", canvasElemImg)

    # --- 3
    # canvasElemImg = cv2.imread(canvasElemImgPath, 1)
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # cv2.imwrite(canvasElemImgFileName + ".3.01.png", canvasElemImg)
    # cv2.imshow('canvasElemImg.3.01', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.3.01')
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imshow('canvasElemImg.3.02', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.3.02')
    # cv2.imwrite(canvasElemImgFileName + ".3.02.png", canvasElemImg)
    # # ---
    # canvasElemImg = cv2.imread(canvasElemImgPath, 1)
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2HSV)
    # cv2.imwrite(canvasElemImgFileName + ".3.03.png", canvasElemImg)
    # cv2.imshow('canvasElemImg.3.03', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.3.03')
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imshow('canvasElemImg.3.04', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.3.04')
    # cv2.imwrite(canvasElemImgFileName + ".3.04.png", canvasElemImg)

    # --- 4
    #   - imread() flags=0 报错。不应使用
    # canvasElemImg = cv2.imread(canvasElemImgPath, 0)
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".4.01.png", canvasElemImg)

    # --- 5
    # canvasElemImg = cv2.imread(canvasElemImgPath, -1)
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # canvasElemImg = abs(255 - canvasElemImg)
    # cv2.imwrite(canvasElemImgFileName + ".5.01.png", canvasElemImg)

    # --- 6
    # canvasElemImg = cv2.imread(canvasElemImgPath, 1)
    # cv2.imwrite(canvasElemImgFileName + ".6.01.png", canvasElemImg)

    # --- 7
    # canvasElemImg = cv2.imread(canvasElemImgPath, 0)
    # cv2.imwrite(canvasElemImgFileName + ".7.01.png", canvasElemImg)

    # --- 8
    # canvasElemImg = cv2.imread(canvasElemImgPath, -1)
    # cv2.imwrite(canvasElemImgFileName + ".8.01.png", canvasElemImg)

    # --- 9
    #   - 发现保存的与渲染展示的图像不一样。当保存的图片后缀为`.jpg`时
    #       - 当保存的图片后缀为`.jpg`后,展示正常
    #   - 关于`.jpg`与`.png`
    #       .jpg 格式是有损压缩，即它的压缩是不可逆的，解压再压缩得到的图片像素值会不同。
    #       而.png是无损压缩，尽可能使用 png 格式吧（输入与输出的图像格式保持一致）。。。
    # canvasElemImg = cv2.imread(canvasElemImgPath, -1) # 加载图像(BGR)，包括alpha通道
    # cv2.imwrite(canvasElemImgFileName + ".9.01.png", canvasElemImg)
    # cv2.imshow('canvasElemImg.9.01', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.9.01')
    # cv2.imwrite(canvasElemImgFileName + ".9.02.jpg", canvasElemImg)
    # cv2.imshow('canvasElemImg.9.02', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.9.02')
    # cv2.imwrite(canvasElemImgFileName + ".9.03.png", canvasElemImg)
    # canvasElemImg = canvasElemImg.astype(np.uint8)
    # cv2.imshow('canvasElemImg.9.03', canvasElemImg)
    # cv2.waitKey()
    # cv2.destroyWindow('canvasElemImg.9.03')

    # --- 10
    # ---1 灰度化处理：方法一
    # canvasElemImg = cv2.imread(canvasElemImgPath, cv2.IMREAD_COLOR)  # 加载彩色图像(BGR)。任何图像的透明度都会被忽视。它是默认标志。
    # cv2.imshow('canvasElemImg.10.01-01', canvasElemImg)
    # canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('canvasElemImg.10.01-02', canvasElemImg)
    # ---2 灰度化处理：方法二
    canvasElemImg = cv2.imread(canvasElemImgPath, cv2.IMREAD_GRAYSCALE)
    cv2.imshow('canvasElemImg.10.01-03', canvasElemImg)

    # ---3 灰度化二值化处理
    #   图像阈值：http://www.woshicver.com/FifthSection/4_3_%E5%9B%BE%E5%83%8F%E9%98%88%E5%80%BC/
    ret, thresh1 = cv2.threshold(canvasElemImg, 185, 255, cv2.THRESH_BINARY)
    cv2.imshow('canvasElemImg.10.01-04', thresh1)
    ret, thresh2 = cv2.threshold(canvasElemImg, 188, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('canvasElemImg.10.01-05', thresh2)
    ret, thresh3 = cv2.threshold(canvasElemImg, 192, 255, cv2.THRESH_TRUNC)
    cv2.imshow('canvasElemImg.10.01-06', thresh3)

    cv2.waitKey()
    cv2.destroyAllWindows()
