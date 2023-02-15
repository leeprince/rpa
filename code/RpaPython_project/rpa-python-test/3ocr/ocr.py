import rpa as r

r.init(visual_automation=True, chrome_browser=False)

print("r.url....")

# 注意：r.init => chrome_browser=False 不能在打开url(r.url(...))
# ./local_web
# 注意：需本地配置 web 服务器
# r.url('http://p.rpa.com/prince_test_html_ocr.html')
# print("r.read....")
# print(r.read("/html/body/div[2]/div/div/div[1]/div[1]/a/img"))

print("r.read....")
# print(r.read("/Users/leeprince/www/python/rpa/code/python/rpa-python-test/ocr/prince_ocr.png"))
print(r.read("prince_number.png"))
# print(r.read("prince_ocr_en.png"))
# print(r.read("prince_ocr_en_zh.png"))

# print("r.read....")
# print(r.read(r.mouse_x(), r.mouse_y(), r.mouse_x() + 400, r.mouse_y() + 200))

print("r.close....")
r.close()
