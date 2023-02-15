import os
import platform
import sys

from selenium import webdriver

from src.service.service import start_tax


def run():
    # 自动更新浏览器的驱动程序
    if not auth_update_webdriver():
        return

    # 初始化 WebDriver
    driver = init_driver()

    # 开始服务
    start_tax(driver)

def auth_update_webdriver():
    """
    自动更新浏览器的驱动程序
    Returns:

    """
    if platform.system() == "Windows":
        # 引入模块
        #   引入模块放在文件顶部，会因为非Windows操作系统的原因报错：`ModuleNotFoundError: No module named 'winreg'`
        from src.utils.windows_auto_import_chromedriver import CheckChromeDriverUpdate
        if not CheckChromeDriverUpdate():
            return False
    if platform.system() in ['Linux', 'Darwin']:  # TODO: 自动检查更新 prince.lee@todo 2022/8/3 16:12
        return True

    return True

def init_driver():
    """
    初始化 WebDriver: 浏览器的驱动程序
    Returns:

    """
    executable_file_name = "chromedriver"
    if platform.system() == "Windows":
        executable_file_name = "chromedriver.exe"

    # 方法一：指定 `chromedriver` 路径
    executable_path = os.path.join(os.path.dirname(os.path.realpath(sys.executable)), executable_file_name)
    if os.path.exists(executable_path):
        print("executable_path:", executable_path)
        # 指定路径
        #   结合：`$ pyinstaller -D --add-binary chromedriver:. main.py` 使用
        driver = webdriver.Chrome(executable_path=executable_path)
    else:
        # 检查当前可执行文件路径是否存在
        executable_path = os.path.join(".", executable_file_name)
        if os.path.exists(executable_path):
            print("executable_path:", executable_path)
            driver = webdriver.Chrome(executable_path)
        else:
            print("executable_path: PATH of default")
            # 默认查找环境变量
            driver = webdriver.Chrome()

    # # 方法二
    # # 解决：python+selenium+chrome 做滑动验证码时，会被浏览器检测到使用的自动软件导致滑动验证失败
    # options = webdriver.ChromeOptions()
    # options.add_argument('--disable-blink-features=AutomationControlled')  # 重点代码：去掉了webdriver痕迹
    # self.driver = webdriver.Chrome(chrome_options=options)
    return driver
