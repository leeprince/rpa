# -*-coding:GBK -*-

import os
import re
import winreg
import zipfile
import requests

base_url = 'http://npm.taobao.org/mirrors/chromedriver/'
version_re = re.compile(r'^[1-9]\d*\.\d*.\d*')  # ƥ��ǰ3λ�汾�ŵ�������ʽ
DEFAULT_CHROME_VERSION = "103.0.5060.134"

def getChromeVersion():
    """ͨ��ע����ѯchrome�汾"""
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Google\\Chrome\\BLBeacon')
        value, t = winreg.QueryValueEx(key, 'version')
        return version_re.findall(value)[0]  # ����ǰ3λ�汾��
    except WindowsError as e:
        # û�а�װchrome�����
        return ""

def getChromeDriverVersion():
    """��ѯChromedriver�汾"""
    outstd2 = os.popen('chromedriver --version').read()
    try:
        version = outstd2.split(' ')[1]
        version = ".".join(version.split(".")[:-1])
        return version
    except Exception as e:
        return "0.0.0"

def getLatestChromeDriver(version):
    # ��ȡ��chrome�汾������driver�汾��
    url = f"{base_url}LATEST_RELEASE_{version}"
    latest_version = requests.get(url).text
    print(f"�뵱ǰchromeƥ�������chromedriver�汾Ϊ: {latest_version}")
    # ����chromedriver
    print("��ʼ����chromedriver...")
    download_url = f"{base_url}{latest_version}/chromedriver_win32.zip"
    file = requests.get(download_url)
    with open("chromedriver.zip", 'wb') as zip_file:  # �����ļ����ű�����Ŀ¼
        zip_file.write(file.content)
    print("�������.")
    # ��ѹ
    f = zipfile.ZipFile("chromedriver.zip", 'r')
    for file in f.namelist():
        f.extract(file)
    print("��ѹ���.")

def CheckChromeDriverUpdate():
    '''
    ��鱾�� chrome �İ汾��������Ѱ�װ�� chromedriver �汾�Ƿ����
        ���ݣ��������
        �����ݣ����� chromedriver �汾
    # TODO: ����ɳɿ�ִ���ļ�ʱ������Զ����ص�·���Ƿ����ִ���ļ���ͬ��Ŀ¼�� prince.lee@todo 2022/8/3 16:12
    ʵ�֣�
        1. ͨ��ע����ѯchrome�汾�ţ�
        2. ��ѯ���ص�chromedriver�汾�ţ�
        3. �鿴�����汾��ǰ��λ�Ƿ�һ�£�����һ�¾͵� http://npm.taobao.org/mirrors/chromedriver/ ��ѯ��ǰchromeƥ�������chromedriver�汾�ţ�
        4. �ϳ��������ӣ�������ز���ѹ��
    :return:
    '''
    chrome_version = getChromeVersion()
    print(f'��ǰchrome�汾: {chrome_version}')
    if chrome_version == "":
        print("������Ҫ��װ���µĹȸ���������汾Ϊ��", DEFAULT_CHROME_VERSION)
        return False
    driver_version = getChromeDriverVersion()
    print(f'��ǰchromedriver�汾: {driver_version}')
    if chrome_version == driver_version:
        print("�汾���ݣ��������.")
        return True
    print("chromedriver�汾��chrome����������ݣ�������>>>")
    try:
        getLatestChromeDriver(chrome_version)
        print("chromedriver���³ɹ�!")
    except requests.exceptions.Timeout:
        print("chromedriver����ʧ�ܣ�������������ԣ�")
        return False
    except Exception as e:
        print(f"chromedriverδ֪ԭ�����ʧ��: {e}")
        return False
