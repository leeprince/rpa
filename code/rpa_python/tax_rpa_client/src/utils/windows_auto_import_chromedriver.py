# -*-coding:GBK -*-

import os
import re
import winreg
import zipfile
import requests

base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # 匹配前3位版本号的正则表达式
DEFAULT_CHROME_VERSION = "103.0.5060.134"

def getChromeVersion():
    """通过注册表查询chrome版本"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # 返回前3位版本号
    except WindowsError as e:
        # 没有安装chrome浏览器
        return ""

def getChromeDriverVersion():
    """查询Chromedriver版本"""
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"

def getLatestChromeDriver(version):
    # 获取该chrome版本的最新driver版本号
    url = f"{base_url}LATEST_RELEASE_{version}"
    latest_version = requests.get(url).text
    print(f"与当前chrome匹配的最新chromedriver版本为: {latest_version}")
    # 下载chromedriver
    print("开始下载chromedriver...")
    download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    file = requests.get(download_url)
    with open("chromedriver.zip", 'wb') as zip_file:  # 保存文件到脚本所在目录
        zip_file.write(file.content)
    print("下载完成.")
    # 解压
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    print("解压完成.")

def CheckChromeDriverUpdate():
    '''
    检查本地 chrome 的版本与程序中已安装的 chromedriver 版本是否兼容
        兼容：无需更新
        不兼容：更新 chromedriver 版本
    # TODO: 当变成成可执行文件时，检查自动下载的路径是否与可执行文件在同级目录下 prince.lee@todo 2022/8/3 16:12
    实现：
        1. 通过注册表查询chrome版本号；
        2. 查询本地的chromedriver版本号；
        3. 查看两个版本号前三位是否一致，若不一致就到 http://npm.taobao.org/mirrors/chromedriver/ 查询当前chrome匹配的最新chromedriver版本号；
        4. 合成下载链接，最后下载并解压。
    :return:
    '''
    chrome_version = getChromeVersion()
    print(f'当前chrome版本: {chrome_version}')
    if chrome_version == "":
        print("本地需要安装最新的谷歌浏览器，版本为：", DEFAULT_CHROME_VERSION)
        return False
    driver_version = getChromeDriverVersion()
    print(f'当前chromedriver版本: {driver_version}')
    if chrome_version == driver_version:
        print("版本兼容，无需更新.")
        return True
    print("chromedriver版本与chrome浏览器不兼容，更新中>>>")
    try:
        getLatestChromeDriver(chrome_version)
        print("chromedriver更新成功!")
    except requests.exceptions.Timeout:
        print("chromedriver下载失败，请检查网络后重试！")
        return False
    except Exception as e:
        print(f"chromedriver未知原因更新失败: {e}")
        return False
