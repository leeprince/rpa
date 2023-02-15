import rpa as r

print("init...")
r.init(visual_automation=True)

print("r.url....")
# ./local_web
# 注意：需本地配置 web 服务器
r.url('http://p.rpa.com/index.html')
r.wait(5)

print("type(600, 300, 'open source')...")
r.type(600, 300, 'open source')
r.wait(5)

print("click(900, 300)...")
r.click(900, 300)
# r.wait(5)

print("snap('page.png', 'results_img_before.png')...")
r.snap('page.png', 'results_img_before.png')
# r.wait(5)

print("hover('images/g10.jpg')...")
r.hover('images/g10.jpg')
# r.wait(5)

print("snap('page.png', 'results_img_after.png')...")
r.snap('page.png', 'results_img_after.png')
# r.wait(5)

print("mouse('down')...")
r.mouse('down')
# r.wait(5)

print("hover(r.mouse_x() + 300, r.mouse_y())...")
r.hover(r.mouse_x() + 300, r.mouse_y())
# r.wait(5)

print("close...")
r.close()