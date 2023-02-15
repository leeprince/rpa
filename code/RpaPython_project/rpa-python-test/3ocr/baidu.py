import rpa as r

r.init()
r.url('https://www.baidu.com')
r.type('//*[@id="kw"]', '新冠肺炎[enter]')
r.wait(1)
r.snap('page', 'baidu_ocr.png')
print(r.read('//*[@id="1"]/div/div[2]/a/div[2]'))

r.close()