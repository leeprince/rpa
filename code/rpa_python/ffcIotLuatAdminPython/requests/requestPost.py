import requests
import json

def getPostTranslateData(translateWord = None):
    #
    #   使用 requests 库请求网站
    #
    # 请求连接
    url = "http://p.ffcbms.com/Msg/send"
    # 设置cookies
    cookies = dict(csc_session="09hlgti1eri1elm741ogr1itc6eo03jr")
    # 数据准备
    FormPostData = {"user_type":"1","user":"","title":"leeprincetest0303","content":translateWord}

    # 请求表单数据
    response = requests.post(url, cookies=cookies, data = FormPostData)
    # 将Json格式字符串转为字典
    # content = json.loads(response.text)
    print(response.text)
    pass

if __name__ == "__main__":
    getPostTranslateData('我爱中国')
