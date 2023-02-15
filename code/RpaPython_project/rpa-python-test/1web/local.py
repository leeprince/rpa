import rpa as r

r.init()

print("r.url....")
# ./local_web
# 注意：需本地配置 web 服务器
r.url('http://p.rpa.com/index.html')

print("r.click....")
r.click('cd-search-trigger')

print("r.type....")
r.type('//*[@name="Search"]', 'programArt[enter]This is...')

print("r.read....")
print(r.read('navbar-brand'))

print("r.snap....")
r.snap('page', 'local_results.png')

print("r.close....")
r.close()

