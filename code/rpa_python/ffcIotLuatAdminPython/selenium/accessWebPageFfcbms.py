from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 访问配置
url = 'http://p.ffcbms.com'
# 登录账户
userName = 'admin'
userpwd = '123456'


# # selenium - webdriver
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# 
driver.get(url)
elemName = driver.find_element_by_name('user_name')
elemPwd = driver.find_element_by_name('password')
elemSubmimt = driver.find_element_by_xpath('//*[@id="form_login"]/div[3]/div/button')

# 键盘输入
elemName.send_keys(userName)
elemPwd.send_keys(userpwd)

# 
# 表单提交 - 方法01
# 
elemSubmimt.submit()
# 
# 表单提交 - 方法02
# 
# elemSubmimt = driver.find_element_by_xpath('//*[@id="form_login"]/div[3]/div/button')
# elemSubmimt.send_keys(Keys.RETURN)

# driver.close()
