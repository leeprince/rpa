import os
import platform
import sys
import time

from selenium import webdriver

class Tax(object):
    """
    python + seleniuum + cv2(opencv)
    """

    def __init__(self, url, driver):
        # 如果是实际应用中，可在此处账号和密码
        self.url = url
        self.driver = driver

    def access_url(self):
        # ssl._create_default_https_context = ssl._create_unverified_context
        driver = self.driver
        driver.maximize_window()
        driver.get(self.url)

        # 业务流程执行完不自动关闭浏览器
        time.sleep(600)

    def after_quit(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

def TaxStartGuangdong(driver):
    # 广东省电子税务局
    url = "https://etax.guangdong.chinatax.gov.cn/sso/login?service=https://etax.guangdong.chinatax.gov.cn/xxmh/html/index_login.html"

    # 初始化税务服务实例
    tax = Tax(url, driver)

    # 访问网站
    tax.access_url()

    print("----------------- TaxStartGuangdong 完成 --------------------")
