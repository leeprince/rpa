import rpa as r

r.init(visual_automation=True)

print("r.url....")
# ./local_web
# 注意：需本地配置 web 服务器
r.url('http://p.rpa.com/index.html')

print("r.dclick....")
r.dclick('cd-search-trigger')

print("r.click....")
r.click('//nav/ul/li/a[@href="about.html"]')

# ...
print("r.type....")
# <input name="q">
r.type('//*[@name="Search"]', 'programArt[enter]This is...')

print("r.close....")
r.close()
