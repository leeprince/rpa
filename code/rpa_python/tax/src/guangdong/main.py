import random
import time

from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By



# >>> 登录相关 《《《《《《《《《《《
# 密码登录元素
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

passLoginBtnElem = '//*[@id="loginQieHuanImg_gddzswjmmdl"]'
# 滑块底图元素
slidingBackElem = '//*[@id="nc_1_wrapper"]'
# 滑块元素
slidingElem = '//*[@id="nc_1_n1z"]'
# 滑块条验证结果
slidingBarElem = '//*[@id="nc_1__scale_text"]/span'
# 滑块到达目标时如果失败会立即触发（未松开左键）的验证错误提示的元素
#   - 根本原因已解决：在 self.access_url() 的方法二中
slidingBarErrElem = '//*[@class="errloading"]'
# 滑块验证结果成功的文本
slidingBarSuccText = '验证通过'

# ---1 账户 。。。。
# 社会信用代码/识别号
taxCodeElem = '//*[@id="shxydmOrsbh"]'
taxCode = '91441302MA55K2xxxx'
# 用户名/实名手机号码
userNameElem = '//*[@id="userNameOrSjhm"]'
userName = 'lgsok'
# 用户密码
userPassElem = '//*[@id="passWord"]'
userPass = 'QF6829xxxx'
# ---1 账户-end 。。。。
# 登录按钮
loginBtnElem = '//*[@id="upLoginButton"]'
# 登录失败的弹窗
loginFailWindowElem = '//*[@class="layui-layer layui-layer-dialog"]/div[2]'
# >>> 登录相关- 《《《《《《《《《《《

class Tax(object):
    """
    python + seleniuum + cv2(opencv)
    """

    def __init__(self, url):
        # 如果是实际应用中，可在此处账号和密码
        self.url = url
        self.driver = None

    def access_url(self):
        # 方法一
        self.driver = webdriver.Chrome()
        # 方法二
        # 解决：python+selenium+chrome 做滑动验证码时，会被浏览器检测到使用的自动软件导致滑动验证失败
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')  # 重点代码：去掉了webdriver痕迹
        self.driver = webdriver.Chrome(chrome_options=options)

        # ssl._create_default_https_context = ssl._create_unverified_context
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)

        # 业务流程执行完不自动关闭浏览器
        # time.sleep(60)

    def after_quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def login_entry(self):
        """
        登录的入口
        :return:
        """
        driver = self.driver
        ieWindow = driver.find_element(by=By.XPATH, value=passLoginBtnElem)
        ieWindow.click()

    def login(self):
        '''
        登录
        :return: 是否登录成功
        '''
        print(">>> 进入登录入口")
        self.login_entry()

        print('>>> 滑动条:请按住滑块，拖动到最右边')
        self.sliding_validate_bar()

        print('>>> 输入账户信息并登录')
        self.account()

    @staticmethod
    def get_track(distance):
        """
        模拟轨迹：模拟人为操作轨迹
        :param distance:
        :return:
        """
        # 初速度
        v = 0
        # 单位时间为0.5s来统计轨迹，轨迹即0.5内的位移
        t = 0.5
        # 位移/轨迹列表，列表内的一个元素代表0.5s的位移
        tracks = []
        # 当前的位移
        current = 0

        distance += 8  # 先滑过一点，最后再反着滑动回来
        # a = random.randint(1,3)
        while current < distance:
            # 加速度越小，单位时间的位移越小,模拟的轨迹就越多越详细
            # 加速运动
            a = random.randint(100, 110)

            # 初速度
            v0 = v
            # 0.5秒时间内的位移.加速度的位移公式：s＝V平t＝Vot+at^2/2＝Vt/2t
            s = v0 * t + 0.5 * a * (t ** 2)
            # 当前的位置
            current += s
            # 添加到轨迹列表
            tracks.append(round(s))

            # 速度已经达到v,该速度作为下次的初速度
            v = v0 + a * t
        return tracks

    def sliding_drag(self, slidIngDragXTrackList):
        """
        按住滑块 》 拖动按住的滑块元素（鼠标左键按向右X方向移动），并按模拟人为操作轨迹进行拖动 》 松开 》 验证是否通过
        :param slidIngDragXTrackList:
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
        # 测试：验证拖动验证失败的场景
        # ActionChains(driver).move_by_offset(xoffset=-40, yoffset=0).perform()
        time.sleep(0.05)

        # 判断是否滑动成功
        print('判断是否滑动成功')
        try:
            WebDriverWait(driver, 0.5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, slidingBarErrElem))
            )
            pass
        except TimeoutException as e:
            print('判断是否滑动成功>获取滑动立即触发的错误：超时》滑动成功！', e.msg)
        else:
            print('判断是否滑动成功>获取滑动立即触发的错误：成功》滑动失败！')
            return False
        finally:
            print('判断是否登录成功>结束')
            pass

        # 松开按住的滑块元素（释放按住的鼠标左键）
        print('松开按住的滑块元素（释放按住的鼠标左键）')
        ActionChains(driver).release(on_element=slidIng).perform()
        time.sleep(0.5)

        # 检查滑动是否验证通过
        drapCodeElemText = driver.find_element(by=By.XPATH, value=slidingBarElem).text
        if drapCodeElemText != slidingBarSuccText:
            print('~~~滑动验证失败~~~')
            return False
        print('***滑动验证成功***')
        return True

    def sliding_validate_bar(self):
        """
        滑动条:请按住滑块，拖动到最右边
        :return:
        """
        driver = self.driver

        # 滑块底图元素
        slidingBack = driver.find_element(by=By.XPATH, value=slidingBackElem)
        # 渲染大小
        slidingBackSize = slidingBack.size
        # 渲染大小的宽
        slidingBackWidth = slidingBackSize['width']

        # 获取滑块元素
        print("获取滑块元素")
        slidIng = driver.find_element(by=By.XPATH, value=slidingElem)
        # 渲染大小
        slidingSize = slidIng.size
        # 渲染大小的宽
        slidIngWidth = slidingSize['width']
        # 渲染大小的宽
        print("获取滑块信息>>>>>\r\n"
              "\t slidingBackSize：%s \r\n"
              "\t slidingBackWidth：%s \r\n"
              "\t slidingSize：%s \r\n"
              "\t slidIngWidth：%s \r\n"
              % (slidingBackSize, slidingBackWidth, slidingSize, slidIngWidth))

        # 计算页面需要拖动的X方向的位移，像素单位：px
        slidIngDragX = slidingBackWidth - slidIngWidth
        print("计算页面需要拖动的X方向的位移，像素单位：px。slidIngDragX>>>>>\r\n"
              "\t slidIngDragX：%s \r\n"
              % (slidIngDragX))

        # 模拟轨迹：模拟人为操作轨迹
        slidIngDragXTrackList = self.get_track(slidIngDragX)
        print(">>>>>\r\n"
              "\t slidIngDragXTrackList：%s \r\n"
              % (slidIngDragXTrackList))

        if not self.sliding_drag(slidIngDragXTrackList):
            print("滑动条:请按住滑块，拖动到最右边验证结果为：失败!")
            self.after_quit()
            return False

        print("滑动条:请按住滑块，拖动到最右边验证结果为：成功!")
        return True

    def account(self):
        """
                输入账号并点击登录
                :return: 登录是否成功
                """
        driver = self.driver

        # 输入账号信息
        print('输入账号信息')
        driver.find_element(by=By.XPATH, value=taxCodeElem).send_keys(taxCode)
        driver.find_element(by=By.XPATH, value=userNameElem).send_keys(userName)
        driver.find_element(by=By.XPATH, value=userPassElem).send_keys(userPass)

        # 点击登录
        print('点击登录')
        driver.find_element(by=By.XPATH, value=loginBtnElem).click()

        # 判断是否登录成功
        print('判断是否登录成功')
        try:
            WebDriverWait(driver, 2).until(
                expected_conditions.visibility_of_element_located((By.XPATH, loginFailWindowElem))
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
            time.sleep(4)
            pass


def TaxStartGuangdong():
    # 广东省电子税务局
    url = "https://etax.guangdong.chinatax.gov.cn/sso/login?service=https://etax.guangdong.chinatax.gov.cn/xxmh/html/index_login.html"

    # 初始化税务服务实例
    tax = Tax(url)

    # 访问网站
    tax.access_url()

    # 登录
    tax.login()


    print("----------------- TaxStartGuangdong 完成 --------------------")
