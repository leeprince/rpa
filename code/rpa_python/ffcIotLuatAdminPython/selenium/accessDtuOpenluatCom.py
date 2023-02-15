import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

''' --------配置-----  '''
# 访问配置
url = 'http://dtu.openluat.com/login'
# 登录账户
userName = 'xxx'
userpwd = 'xxx'

# dtu参数配置
groupList = [866262045283966]
# 产品key
ProductKey = 'a1Z7iyxdBpi'
# 设备密钥
DeviceSecret = 'JBn6pPofGOVfts2CwF8JnUBJBmCYUqd7'
# 设备名称
DeviceName = groupList[0]
# 链接保活时间
linkKeeppAlive = 60
# 主题列表
topicDict = {'sub':'sys/${ProductKey}/${DeviceName}/rrpc/request/+', 'pub':'/sys/${ProductKey}/${DeviceName}/rrpc/response/${messageId}'}

''' --------配置-end----- '''

# # selenium - webdriver
# 打开相应浏览器驱动
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

driver.implicitly_wait(5)

# 访问url
driver.get(url)

# 登录账号键盘输入
elemName = driver.find_element_by_id('name_Login')
elemName.send_keys(userName)
elemPwd = driver.find_element_by_id('password_Login')
elemPwd.send_keys(userpwd)

# 登录表单提交
elemSubmimt = driver.find_element(by=By.XPATH, value='//*[@id="react-container"]/div/div/div/div/form/div[3]/button')
# 登录表单提交 - 方法01
# elemSubmimt.submit()
# 登录表单提交 - 方法02 [推荐]
elemSubmimt.send_keys(Keys.RETURN)
print('登录表单提交')

# 点击切换分组管理
switchMenu = driver.find_element(by=By.XPATH, value='//*[@id="0$Menu"]/li[2]')
switchMenu.click()
print('点击切换分组管理')

# ''' -------------新建分组-----------------
# 新建分组
# 点击新建分组按钮
newGroup = driver.find_element(by=By.CLASS_NAME, value='addEquipment')
newGroup.click()
print('点击新建分组按钮')
# 输入分组名称
inputGroup = driver.find_element(by=By.CLASS_NAME, value='ant-input')
inputGroup.send_keys(groupList[0])
print('输入分组名称')

# 提交分组
submitGroup = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div[2]/div/div[1]/div[3]/button[2]')
submitGroup.click()
print('提交分组')

closeGroupModal = driver.find_element(by=By.CLASS_NAME, value='ant-modal-close-x')
closeGroupModal.click()
# ''' -------------新建分组-----------------

class canClickMachineView():
    def __init__(self):
        pass
    def __call__(self, driver):
        isSpin = False
        try:
            spin = driver.find_element(By.CLASS_NAME, 'ant-spin-container ant-spin-blur')
            pass
        except NoSuchElementException as e:
            print('spin-已不存在')
            isSpin = True
        else:
            print('spin-else')
            pass
        finally:
            pass
        
        isFade = False
        try:
            fade = driver.find_element(By.CLASS_NAME, 'fade-leave fade-leave-active')
            pass
        except NoSuchElementException as e:
            print('fade-已不存在')
            isFade = True
        else:
            print('fade-else')
            pass
        finally:
            pass

        if isSpin and isFade:
            return True
        else:
            return False

# 查看设备列表
try:
    # 隐式等待和显示等待都存在时，超时时间取二者中较大的
    # 显示等待：WebDriverWait(driver, time).unitl()；隐式等待：driver.implicitly_wait()
    # 等待方法1: 出现不稳定的情况，不推荐
    # waitEle = WebDriverWait(driver, 10).until(
    #     # 【不可用】通过元素是否存在；实际条件并非如此；不使用
    #     # EC.presence_of_element_located((By.CLASS_NAME, 'ant-spin-nested-loading'))
    #     # EC.presence_of_all_elements_located((By.CLASS_NAME, 'ant-spin-nested-loading'))
    #     # EC.visibility_of_element_located((By.CLASS_NAME, 'ant-spin-nested-loading'))
    #     # 【不可用】通过元素是否可以点击; 会报错，因为会被 class='ant-spin-container  ant-spin-blur' 的点击给截获；不使用
    #     # EC.element_to_be_clickable((By.XPATH, '//*[@id="react-container"]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[last()]/td[5]/div/button[2]'))
    #     # 【可用】通过判断遮罩层的类名：class='ant-spin-container  ant-spin-blur'
    #     EC.invisibility_of_element_located((By.CLASS_NAME, 'ant-spin-container ant-spin-blur'))
    #     # 【可用】通过遮罩层淡出的类名：class = 'fade-leave fade-leave-active'
    #     # EC.invisibility_of_element_located((By.CLASS_NAME, 'fade-leave fade-leave-active'))
    # )
    # 等待方法2: 将以上两种可用的方法定义到自定义等待条件中， 推荐
    waitEle = WebDriverWait(driver, 10).until(
        canClickMachineView()
    )

    viewGroupDevice = driver.find_element(by=By.XPATH, value='//*[@id="react-container"]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[last()]/td[5]/div/button[2]')
    viewGroupDevice.click()
    print('查看设备列表')
except Exception as e:
    print('>查看设备列表-捕获异常！！！！！！！', e)
    time.sleep(1)
    # xpath最后一个元素：last();;tr[last()]
    viewGroupDeviceEle = driver.find_element(by=By.XPATH, value='//*[@id="react-container"]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[last()]/td[5]/div/button[2]')
    viewGroupDeviceEle.click()
    print('重新查看设备列表')

# 添加设备
addDevice = driver.find_element(by=By.CLASS_NAME, value='addEquipment')
addDevice.click()
time.sleep(2)
print('添加设备')

# 点击列表选择添加
listAddDevice = driver.find_element(by=By.CSS_SELECTOR, value='div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)')
listAddDevice.click()
time.sleep(1)
print('点击列表选择添加')

# 输入Imei
try:
    waitEle = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'ant-calendar-picker'))
    )
    inputImei = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > input')
    inputImei.send_keys(groupList[0])
    print('输入Imei')
except Exception as e:
    print('>输入Imei-捕获异常', e)
    quit()

# 搜索
findImei = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > button')
findImei.click()
print('搜索添加')

# 点击选择Imei
try:
    waitEle = WebDriverWait(driver, 10).until(
        canClickMachineView()
    )
    selectFindImei = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div > div > div > div > div > div.ant-table-body > table > thead > tr > th.ant-table-selection-column > span > div > label > span > input')
    selectFindImei.click()
    print('点击选择Imei')
    pass
except Exception as e:
    print('>捕获点击选择Imei异常', e)
    selectFindImei = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div > div > div > div > div > div.ant-table-body > table > thead > tr > th.ant-table-selection-column > span > div > label > span > input')
    selectFindImei.click()
    print('重新点击选择Imei')

time.sleep(1)
# 确定添加imei为分组设备
# 选择属于其父元素最后一个子元素：last-child
# body > div:nth-child(4) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button 修改为 body > div:last-child > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button
confirmAddDevice = driver.find_element(by=By.CSS_SELECTOR, value='body > div:last-child > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button')
confirmAddDevice.click()
time.sleep(1)
print('确定添加imei为分组设备')

# 返回
returnGoupList = driver.find_element(by=By.XPATH, value='//*[@id="react-container"]/div/div/div[2]/div[2]/div/div/div/a')
returnGoupList.click()


# 点击参数配置
# xpath最后一个元素：last();;tr[last()]
parameterConfig = driver.find_element(by=By.XPATH, value='//*[@id="react-container"]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr[last()]/td[5]/div/button[1]')
parameterConfig.click()
print('点击参数配置')
time.sleep(1)

# 点击串口参数
# # 页面刷新
# body > div:nth-child(4) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)
# # 页面不刷新
# body > div:nth-child(6) > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)
# 为兼容页面是否刷新，将变动的前部分：body > div:nth-child(6) > div >  去掉
portConfig = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(3)')

portConfig.click()
time.sleep(1)
print('点击串口参数')

# 启动串口1
selectPort01 = driver.find_element(by=By.CSS_SELECTOR, value='div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > label:nth-child(1) > span.ant-radio > input')
selectPort01.click()
print('启动串口1')

# 选择网络通道参数
netConfig = driver.find_element(by=By.CSS_SELECTOR, value='div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-bar > div > div > div > div > div:nth-child(4)')
netConfig.click()
print('选择网络通道参数')
time.sleep(1)

# 启动通道1
selectNet01 = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ant-radio-group > label.ant-radio-wrapper.ant-radio-wrapper-checked > span.ant-radio.ant-radio-checked > input')
selectNet01.click()
time.sleep(1)
print('启动通道1')
selectNet01 = driver.find_element(by=By.XPATH, value='/html/body/div[last()]/div/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/label[1]/span[1]/input')
selectNet01.click()
time.sleep(1)
print('重新启动通道1')


# 选择通道类型
aliTypeEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div.parameWrap > div > label:nth-child(5) > span.ant-radio > input')
aliTypeEle.click()
# 选择注册类型
regTypeEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div > label:nth-child(3) > span.ant-radio > input')
regTypeEle.click()
# 链接保活时间
linkKeeppAliveEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > input')
linkKeeppAliveEle.clear()
linkKeeppAliveEle.send_keys(linkKeeppAlive)
# ProductKey
ProductKeyEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(1) > input')
ProductKeyEle.clear()
ProductKeyEle.send_keys(ProductKey)
# DeviceSecret
DeviceSecretEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(2) > input')
DeviceSecretEle.clear()
DeviceSecretEle.send_keys(DeviceSecret)
# DeviceName
DeviceNameEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(3) > input')
DeviceNameEle.clear()
DeviceNameEle.send_keys(DeviceName)
# 产品版本类型
aliVersionEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > div:nth-child(4) > div > label:nth-child(2) > span.ant-radio > input')
aliVersionEle.click()
# 订阅主题
subTopicEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > input')
subTopicEle.clear()
subTopicEle.send_keys(topicDict['sub'])
# 发布主题
pubTopicEle = driver.find_element(by=By.CSS_SELECTOR, value='div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div > div.ant-tabs-content.ant-tabs-content-animated > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div:nth-child(2) > div:nth-child(2) > div:nth-child(7) > input')
pubTopicEle.clear()
pubTopicEle.send_keys(topicDict['pub'])
# 确定配置文件
# 选择属于其父元素最后一个子元素：last-child
confirmConfigEle = driver.find_element(by=By.CSS_SELECTOR, value='body > div:last-child > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.ant-btn.ant-btn-primary.ant-btn-lg')
confirmConfigEle.click()
print('确定配置文件')

print('完成DTU后台配置')

# 等待时间
# time.sleep(30)

# 终止程序
# 两种方法
# exit()
# quit()

# 关闭浏览器 - 方法01
# driver.close()
# 关闭浏览器 - 方法02
driver.quit()
