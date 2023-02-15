import rpa as r

r.init()

print("r.url....")
r.url('https://www.baidu.com')

print("r.type....")
# <input name="wd">
r.type('//*[@name="wd"]', 'golang[enter]')

print("r.read....")
# class="hint_PIwZX c_font_2AD7M"
print(r.read('hint_PIwZX c_font_2AD7M'))

print("r.snap....")
r.snap('page', 'baidu_results.png')

print("r.close....")
r.close()

