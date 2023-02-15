import requests
from bs4 import BeautifulSoup

def getHtml():
    #
    #   使用 requests 库请求网站
    #
    # 请求的url
    url = "http://www.cntour.cn/"
    # 获取url地址源码
    strhtml = requests.get(url)
    # print(strhtml.text)

    # 
    # 使用 Beautiful Soup 解析网页... 通过 requests 库已经可以抓到网页源码，接下来要从源码中找到并提取数据。Beautiful Soup 是 python 的一个库，其最主要的功能是从网页中抓取数据。Beautiful Soup 目前已经被移植到 bs4 库中，也就是说在导入 Beautiful Soup 时需要先安装 bs4 库。
    #
    # beautiful soup解析源码, 并使用lxml解析器进行解析
    soup = BeautifulSoup(strhtml.text, 'lxml')
    # 选择器定位数据..
    data = soup.select('#main > div > div.navBox.mtop > ul > li > a')
    # print(data)
    # 清洗数据...提取标签的正文用 get_text() 方法;提取标签中的属性用 get('xxx') 方法
    resultData = []
    for item in data:
        result = {
            'title': item.get_text(),
            'link': item.get('href'),
        }
        resultData.append(result)

    print(resultData)

if __name__ == "__main__":
    getHtml()