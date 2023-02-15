#!/usr/local/bin/python3
import qrcode

codeList = ['f100', 'f101', 'f102']

# 批量生成二维码
def createBatchQrcode(codeList):
    usrPrefix = "https://f.qkc88.cn/userwxapp?c="

    for x in codeList:
        # 二维码内容
        content = usrPrefix + x

        # 生成二维码
        img = qrcode.make(content)

        # 重命名文件名
        imgName = x + '.png'

        # 文件保存路径
        imgPath = './qrcodeImg/'

        # 直接显示图片
        # img.show()
        
        # 保存二维码为文件
        img.save(imgPath+imgName)

        pass
    pass

createBatchQrcode(codeList)