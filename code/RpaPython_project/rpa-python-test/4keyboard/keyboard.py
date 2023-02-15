import rpa as r

print("init...")
r.init(visual_automation=True, chrome_browser=False)

print("keyboard...")
r.keyboard('[cmd][space]')

print("keyboard...")
r.keyboard('safari[enter]')

print("keyboard...")
r.keyboard('[cmd]t')

print("keyboard...")
r.keyboard('snatcher[enter]')

print("keyboard...")
r.wait(0.5)

print("snap...")
r.snap('page.png', 'results.png')

print("close...")
r.close()
