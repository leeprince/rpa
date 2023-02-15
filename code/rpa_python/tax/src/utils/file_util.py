import base64
import os.path


def imagesBase64ToSaveFile(imgBase64, toSaveFileName):
    """
    图片的base64保存为图片
    :param imgBase64: 图片 base64 字符串。可能包含 base64 的图片头部标识`data:image/png;base64,`
    :param toSaveFileName:  保存的
    :return:
    """
    # 替换 `%0D%0A` 换行符
    imgOriginBase64 = str(imgBase64).replace('%0D%0A', "")
    # 去除 base64 的图片头部标识
    imgList = imgOriginBase64.split(';base64,')
    if len(imgList) >= 2:
        imgOriginBase64 = imgList[1]

    imgdata = base64.b64decode(imgOriginBase64)
    file = open(toSaveFileName, 'wb')
    file.write(imgdata)
    file.close()

def fileToBase64(filePath):
    pic = open(filePath, "rb")
    pic_base64 = base64.b64encode(pic.read())
    pic.close()
    return pic_base64

def getNewFilePathByFilePath(filePath, newFileNamePrefix="tmp."):
    '''
    通过原文件路径（包含文件名）获取到新的文件路径（同样的保存路径，不一样的文件名称）
    :param filePath:    原文件路径及包含文件名
    :param newFileNamePrefix: 新的文件名的前缀
    :return: 新的文件名（同样的保存目录）
    '''
    fileName = os.path.basename(filePath)
    fileDir = os.path.dirname(filePath)

    fileNameData = fileName.split(".")
    fileNameName = str(".").join(fileNameData[:-1])
    fileNameExt = fileNameData[-1]

    newFileName = str("{}.{}.{}").format(fileNameName, newFileNamePrefix, fileNameExt)

    return os.path.join(fileDir, newFileName)
