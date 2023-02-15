import numpy as np
import random

# import requests
from selenium.webdriver import ActionChains
import time
from selenium import webdriver
import os
from selenium.webdriver.support.ui import WebDriverWait
import cv2
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# +++++++++++++++++++++++登录相关+++++++++++++++++++++++
# IE内核弹窗提示
popupElem = '//*[@id="layui-layer1"]/div[3]/a'
# 登录的入口
loginEntryElem = '//*[@id="middle_item_02"]'
# --- 相关元素 XPath ---
# 遮罩图（滑块背景图）
from tax.src.utils.chaojiying.chaojiying import Chaojiying_Client
from tax.src.utils import file_util

canvasElem = '//*[@id="canvas"]'  # 企业登录
# canvasElem = '//*[@id="canvas_zrr"]'  # 自然人登录
# 裁剪图（滑块图）
blockElem = '//*[@id="block"]'  # 企业登录
# blockElem = '//*[@id="block_zrr"]'  # 自然人登录
# 滑块元素
slidingElem = '//*[@id="btn"]'  # 企业登录
# slidingElem = '//*[@id="btn_zrr"]"]'  # 自然人登录
# 滑动验证码结果
drapCodeElem = '//*[@id="text"]'
# 滑动验证码结果成功的文本
drapCodeElemSuccText = '验证通过'
# --- 相关元素 XPath -end ---

# --- 图片保存路径 ---
# 遮罩图（滑块背景图）保存路径
#   - 当前时间戳
ctime = str(int(time.mktime(time.localtime())))
canvasElemImgPath = str("./src/shandong/image/validate_code/canvasElemImg.{}.png").format(ctime)
# 裁剪图（滑块图）保存路径
blockElemImgPath = str("./src/shandong/image/validate_code/blockElemImg.{}.png").format(ctime)
# --- 图片保存路径-end ---

# <<< 登录账号相关 <<<<<<<<<<<<<<<<<<<<<
# <<<1 山东电子税务局账号元素信息
# 请输入社会信用代码/识别号
loginTaxCodeElem = '//*[@id="userId"]'
# 请输入手机号/身份证号码/操作员代码
loginUserIdElem = '//*[@id="czydm"]'
# 请输入密码（法定代表人、财务负责人、办税人员）
loginUserPassElem = '//*[@id="password"]'
# 登录按钮
loginBtnElem = '//*[@id="zrrLogin"]'
# 登录失败弹窗
loginFailLayerElem = '//*[@id="layui-layer1"]'
# <<<1 山东电子税务局账号元素信息-end

# <<<2 山东电子税务局账号信息
# 请输入社会信用代码/识别号
loginTaxCode = "91371700MA3WC6T91B"
# 请输入手机号/身份证号码/操作员代码
loginUserId = "37292919820711xxxx"
# 请输入密码（法定代表人、财务负责人、办税人员）
loginUserPass = "Aa666xxxxx"

# <<<2 山东电子税务局账号信息-end
# <<< 登录账号信息-end <<<<<<<<<<<<<<<<<<<<<
# +++++++++++++++++++++++登录相关-end+++++++++++++++++++++++

class Tax(object):
    """
    python + seleniuum + cv2(opencv)
    """

    def __init__(self, url):
        # 如果是实际应用中，可在此处账号和密码
        self.url = url
        self.driver = None

    @staticmethod
    def get_position(canvasElemImgPath, blockElemImgPath):
        """canvasElemImgPath, blockElemImgPath
        判断缺口位置
        :param canvasElemImgPath: 遮罩图的文件路径
        :param blockElemImgPath: 裁剪图的文件路径
        :return: 位置 x, y
        """
        canvasElemImg = cv2.imread(canvasElemImgPath, 0)
        blockElemImg = cv2.imread(blockElemImgPath, 0)

        # 展示圈出来的区域时需要的变量。不需要展示
        # w, h = canvasElemImgFirst.shape[::-1]

        cv2.imwrite(file_util.getNewFilePathByFilePath(canvasElemImgPath, "cv.00"), canvasElemImg)
        canvasElemImg = cv2.imread(file_util.getNewFilePathByFilePath(canvasElemImgPath, "cv.00"))
        canvasElemImg = cv2.cvtColor(canvasElemImg, cv2.COLOR_BGR2GRAY)
        canvasElemImg = abs(255 - canvasElemImg)
        cv2.imwrite(file_util.getNewFilePathByFilePath(canvasElemImgPath, "cv.01"), canvasElemImg)
        canvasElemImg = cv2.imread(file_util.getNewFilePathByFilePath(canvasElemImgPath, "cv.01"))

        cv2.imwrite(file_util.getNewFilePathByFilePath(blockElemImgPath, "cv.00"), blockElemImg)
        blockElemImg = cv2.imread(file_util.getNewFilePathByFilePath(blockElemImgPath, "cv.00"))

        result = cv2.matchTemplate(canvasElemImg, blockElemImg, cv2.TM_CCOEFF_NORMED)
        x, y = np.unravel_index(result.argmax(), result.shape)
        return x, y

        # # 展示圈出来的区域
        # print("展示圈出来的区域")
        # print(">>>>>\r\n"
        #       "\t x：%s \r\n"
        #       "\t y：%s \r\n"
        #       "\t w：%s \r\n"
        #       "\t h：%s \r\n"
        #       % (x, y, w, h))
        # cv2.rectangle(blockElemImg, (y, x), (y + w, x + h), (7, 249, 151), 2)
        # cv2.imwrite("yuantu.jpg", blockElemImg)
        # show(blockElemImg)
        # return x, y

    @staticmethod
    def get_position_of_chaojiying(filePath=canvasElemImgPath):
        """
        通过超级鹰API返回裁剪图的坐标
        :param filePath: 遮罩图的路径
        :return:    返回裁剪图的坐标
        """
        chaojiyingCli = Chaojiying_Client(username="用户名XXX", pass2="密码XXX", soft_id="901598")
        canvasElemImgBase64 = file_util.fileToBase64(filePath)
        if canvasElemImgBase64 == "":
            return None
        data = chaojiyingCli.PostPic_base64(canvasElemImgBase64, "9101")
        if data['err_no'] != 0:
            print("get_position_of_chaojiying>>>>>>> [failed]\r\n"
                  "\t data：%s \r\n"
                  % (data))
            return None
        picStr = data["pic_str"]

        x, y = picStr.split(",")
        return int(y), int(x)

    @staticmethod
    def get_track(distance):
        """
        模拟轨迹：模拟人为操作轨迹
        :param distance:
        :return:
        """
        # 初速度
        v = 0
        # 单位时间为0.2s来统计轨迹，轨迹即0.2内的位移
        t = 0.2
        # 位移/轨迹列表，列表内的一个元素代表0.2s的位移
        tracks = []
        # 当前的位移
        current = 0
        # 到达mid值开始减速
        mid = distance * 7 / 8

        distance += 8  # 先滑过一点，最后再反着滑动回来
        # a = random.randint(1,3)
        while current < distance:
            if current < mid:
                # 加速度公式：a＝(Vt-Vo)/t
                # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
                # 加速运动
                if distance >= 150:
                    a = random.randint(20, 22)
                else:
                    a = random.randint(8, 10)  # 加速运动
            else:
                # 减速运动
                if distance >= 150:
                    a = -random.randint(16, 18)
                else:
                    a = -random.randint(6, 8)

            # 初速度
            v0 = v
            # 0.2秒时间内的位移.加速度的位移公式：s＝V平t＝Vot+at^2/2＝Vt/2t
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v = v0 + a * t

        # 反着滑动到大概准确位置
        for i in range(4):
            tracks.append(-random.randint(2, 3))
        for i in range(4):
            tracks.append(-random.randint(1, 3))
        return tracks

    def after_quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def access_url(self):
        """
        访问网站
        :return:
        """
        self.driver = webdriver.Chrome()

        # ssl._create_default_https_context = ssl._create_unverified_context
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)

        # 业务流程执行完不自动关闭浏览器
        # time.sleep(60)

    def close_ie_popup(self):
        """
        关闭IE内核弹窗提示
        :return:
        """
        time.sleep(2)
        driver = self.driver
        ieWindow = driver.find_element(by=By.XPATH, value=popupElem)
        ieWindow.click()

    def login_entry(self):
        """
        登录的入口
        :return:
        """
        driver = self.driver
        ieWindow = driver.find_element(by=By.XPATH, value=loginEntryElem)
        ieWindow.click()

    def sliding_drag(self, slidIngDragXTrackList, fineTuningX=0):
        """
        按住滑块 》 拖动按住的滑块元素（鼠标左键按向右X方向移动），并按模拟人为操作轨迹进行拖动 》 松开 》 验证是否通过
        :param slidIngDragXTrackList:
        :param fineTuningX:
        :return:
        """
        driver = self.driver

        # 获取滑块元素
        print("获取滑块元素")
        time.sleep(0.05)
        slidIng = driver.find_element(by=By.XPATH, value=slidingElem)

        # 按住滑块元素（鼠标左键点击并按住）
        print("按住滑块元素（鼠标左键点击并按住）")
        ActionChains(driver).click_and_hold(on_element=slidIng).perform()
        time.sleep(0.05)

        print("拖动按住的滑块元素（鼠标左键按住后移动），并按模拟人为操作轨迹进行拖动中...")
        for trackX in slidIngDragXTrackList:
            # 拖动滑块元素(x,y)
            ActionChains(driver).move_by_offset(xoffset=trackX, yoffset=0).perform()  # 鼠标移动到距离当前位置
        # 最后根据实际情况微调拖动滑块元素
        # ActionChains(driver).move_by_offset(xoffset=-random.randint(0, 1), yoffset=0).perform()
        print("最后根据实际情况微调拖动滑块元素.微调像素：", fineTuningX)
        ActionChains(driver).move_by_offset(xoffset=fineTuningX, yoffset=0).perform()
        # 测试：验证拖动验证失败的场景
        # ActionChains(driver).move_by_offset(xoffset=-40, yoffset=0).perform()
        time.sleep(0.05)

        # 松开按住的滑块元素（释放按住的鼠标左键）
        print('松开按住的滑块元素（释放按住的鼠标左键）')
        ActionChains(driver).release(on_element=slidIng).perform()
        time.sleep(0.5)

        # 检查滑动是否验证通过
        drapCodeElemText = driver.find_element(by=By.XPATH, value=drapCodeElem).text
        if drapCodeElemText != drapCodeElemSuccText:
            print('~~~滑动验证失败~~~')
            return False

        print('***滑动验证成功***')
        return True

    def login(self):
        """
        登录
        :return: 是否登录成功
        """

        # 直接访问登陆界面的情况下，无需关闭弹窗提示及点击登录入口
        # print("关闭弹窗提示")
        # self.close_ie_popup()
        # print("进入登录入口")
        # self.login_entry()

        print(">>> 按住左边滑块,拖动完成上方拼图...")
        validate_code_num = 0
        while True:
            validate_code_num += 1
            # 电子税务局每张滑动验证码的允许最大尝试次数为3次。都尝试失败之后会重新刷新
            print("> 滑动验证码刷新次数：", validate_code_num)
            if not self.sliding_validate_code():
                print("login》validate_code 滑块拖动验证结果为：失败!")
                # 直到滑动验证成功，不再关闭浏览器
                # self.after_quit()
                continue
            break
        print("login》validate_code 按住左边滑块,拖动完成上方拼图验证结果为：成功! 滑动验证码刷新次数：", validate_code_num)

        print(">>> 输入账号登录")
        if not self.account():
            print("login》account 输入账号登录：失败!")
            self.after_quit()
            return False
        print("login》account  输入账号登录：成功!")

    def account(self):
        """
        输入账号并点击登录
        :return: 登录是否成功
        """
        driver = self.driver

        # 输入账号信息
        print('输入账号信息')
        driver.find_element(by=By.XPATH, value=loginTaxCodeElem).send_keys(loginTaxCode)
        driver.find_element(by=By.XPATH, value=loginUserIdElem).send_keys(loginUserId)
        driver.find_element(by=By.XPATH, value=loginUserPassElem).send_keys(loginUserPass)

        # 点击登录
        print('点击登录')
        driver.find_element(by=By.XPATH, value=loginBtnElem).click()

        # 判断是否登录成功
        print('判断是否登录成功')
        try:
            WebDriverWait(driver, 2).until(
                expected_conditions.visibility_of_element_located((By.XPATH, loginFailLayerElem))
            )
            pass
        except NoSuchElementException as e:
            print('判断是否登录成功>登录失败弹窗：不存在》登录成功！', e.msg)
            return True
        except TimeoutException as e:
            print('判断是否登录成功>获取登录失败弹窗：超时》登录成功！', e.msg)
            return True
        # except (NoSuchElementException, TimeoutException) as e:
        #     print('判断是否登录成功>登录失败弹窗：不存在 or 超时》登录成功！', e.msg)
        #     return True
        else:
            print('判断是否登录成功>登录失败弹窗：存在》登录失败！')
            return False
        finally:
            print('判断是否登录成功>结束')
            pass

    def sliding_validate_code(self):
        """
        滑动验证码:按住左边滑块,拖动完成上方拼图
        :return: 滑动验证成功
        """
        driver = self.driver

        # -------------------- 获取 遮罩图/裁剪图 元素是 base64 直接渲染，无法获取相关尺寸 ----------------------
        # # 获取 遮罩图/裁剪图 元素的尺寸
        # print("获取遮罩图/裁剪图 元素的尺寸")
        # canvasElemData = driver.find_element(by=By.XPATH, value=canvasElem)
        # 渲染大小
        # canvasElemSize = canvasElemData.size
        # 渲染大小的宽
        # canvasElemWidth = canvasElemSize['width']
        # 元素在可渲染画布中的位置
        # canvasElemX = canvasElemData.location['x']
        # blockElemData = driver.find_element(by=By.XPATH, value=blockElem)
        # blockElemX = blockElemData.location['x']
        # print(">>>>>\r\n"
        #       "\t canvasElemData：%s \r\n"
        #       "\t canvasElemSize：%s \r\n"
        #       "\t canvasElemWidth：%s \r\n"
        #       "\t canvasElemX：%s \r\n"
        #       "\t blockElemData：%s \r\n"
        #       "\t blockElemX：%s \r\n"
        #       % (canvasElemData, canvasElemSize, canvasElemWidth, canvasElemX, blockElemData, blockElemX))
        # --------------------  获取 遮罩图/裁剪图 元素是 base64 直接渲染，无法获取相关尺寸-end ----------------------

        # 获取 遮罩图/裁剪图 元素的图片base64
        time.sleep(0.2)
        print("获取遮罩图/裁剪图 元素的图片base64")
        #   - 滑块背景图（遮罩图）
        canvasElemImgBase64 = driver.find_element(by=By.XPATH, value=canvasElem).get_attribute('src')  # 图片 base64
        #   - 裁剪图（滑块图）
        blockElemImgBase64 = driver.find_element(by=By.XPATH, value=blockElem).get_attribute('src')  # 图片 base64

        # 遮罩图/裁剪图 元素的图片base64保存为图片
        print("遮罩图/裁剪图 元素的图片base64保存为图片")
        # print("canvasElemImgBase64：", canvasElemImgBase64)
        # print("blockElemImgBase64：", blockElemImgBase64)
        os.makedirs('./src/shandong/image/validate_code/', exist_ok=True)
        # 遮罩图
        file_util.imagesBase64ToSaveFile(canvasElemImgBase64, canvasElemImgPath)
        # 裁剪图
        file_util.imagesBase64ToSaveFile(blockElemImgBase64, blockElemImgPath)

        # 通过已保存的本地 遮罩图/裁剪图，获取位置信息
        print("通过已保存的本地遮罩图/裁剪图，获取位置信息")
        # --- 无需以下元素的真实尺寸信息
        # # 遮罩图
        # canvasElemImg = Image.open(canvasElemImgPath)
        # # 遮罩图的真实尺寸。0:宽度；1:高度
        # canvasElemImgRealWidth = canvasElemImg.size[0]
        # # 裁剪图
        # blockElemImg = Image.open(blockElemImgPath)
        # # 裁剪图的真实尺寸。0:宽度；1:高度
        # blockElemImgRealWidth = blockElemImg.size[0]
        # print(">>>>>\r\n"
        #       "\t canvasElemImgRealWidth：%s \r\n"
        #       "\t blockElemImgRealWidth：%s \r\n"
        #       % (canvasElemImgRealWidth, blockElemImgRealWidth))
        # --- 无需元素的真实尺寸信息-end

        # ---d 获取遮罩图中裁剪图的位置
        # 遮罩图中存在裁剪图的所在的位置。返回的 (x, y) 对应的 (y, x) 元组，即 y=position[0] x=position[1]
        # opencv:通过 opencv 模板匹配
        # position = self.get_position(canvasElemImgPath, blockElemImgPath)
        # 超级鹰:通过 超级鹰 接口调用返回遮罩图中的裁剪图坐标
        position = self.get_position_of_chaojiying(canvasElemImgPath)
        if not position:
            print('!!!!>>>>>>>>>>>>>position failed:not position')
            return
        # ---d 获取遮罩图中裁剪图的位置-end

        # 计算页面需要拖动的X方向的位移，像素单位：px
        slidIngDragX = position[1]
        print("计算页面需要拖动的X方向的位移，像素单位：px。slidIngDragX>>>>>\r\n"
              "\t position：%s \r\n"
              "\t slidIngDragX：%s \r\n"
              % (position, slidIngDragX))

        # print("调试》终端>>>>>>>>>>>>>>>>>>>")
        # time.sleep(3)
        # # self.after_quit()
        # return
        # print("调试》终端>>>>>>>>>>>>>>>>>>>-end")

        # 模拟人为操作轨迹
        print("模拟人为操作轨迹")
        slidIngDragXTrackList = self.get_track(slidIngDragX)
        print(">>>>>\r\n"
              "\t slidIngDragXTrackList：%s \r\n"
              % (slidIngDragXTrackList))

        # 按住滑块 》 拖动按住的滑块元素（鼠标左键按向右X方向移动），并按模拟人为操作轨迹进行拖动 》 松开 》 验证是否通过
        sildIngCheckNum = 0
        sildIngCheckNumMax = 3  # 电子税务局每张滑动验证码允许最大尝试次数为3次。都尝试失败之后会重新刷新
        fineTuningStepX = 0  # 每次失败添加向左微调像素（单位px）
        sildIngCheckResult = False
        while not sildIngCheckResult and sildIngCheckNum < sildIngCheckNumMax:
            fineTuningStepX += 1.5
            sildIngCheckNum += 1
            if self.sliding_drag(slidIngDragXTrackList, -fineTuningStepX):
                sildIngCheckResult = True
                break
            print("按住左边滑块,拖动完成上方拼图验证失败后，继续尝试，已执行次数：", sildIngCheckNum)
        if sildIngCheckResult:
            print("按住左边滑块,拖动完成上方拼图验证结果为：成功! 已执行次数：", sildIngCheckNum)
        else:
            print("按住左边滑块,拖动完成上方拼图验证结果为：失败! 已执行次数：", sildIngCheckNum)
        return sildIngCheckResult


def TaxStartShandong():
    # 山东省电子税务局：需关闭IE内核提示弹窗
    # url = "https://etax.shandong.chinatax.gov.cn/"
    # 山东省电子税务局：直接访问
    url = "https://etax.shandong.chinatax.gov.cn/enterprise/dzswjlogin/dzswj_login.jsp?type=wybs"

    # 初始化税务服务实例
    tax = Tax(url)

    # 访问网站
    tax.access_url()

    # 登录
    tax.login()


    print("----------------- TaxStartShandong 完成 --------------------")
