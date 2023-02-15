import requests
import json
from fake_useragent import UserAgent

def getPostTranslateData(groupName = None):
    #
    #   使用 requests 库请求网站
    #
    # 请求连接
    url = "http://dtu.openluat.com/api/site/group"
    # 设置请求头; 三种方式都行；推荐使用最简单的
    ua = (UserAgent()).random
    # 设置请求头 - User-Agent | Referer | Content-Type
    # Content-Type{'Content-Type':'application/json;charset=UTF-8'} | {'content-type':'text/html;charset=UTF-8'}
    # headers = {'User-Agent': ua, 'Referer': 'http://dtu.openluat.com/groupmanage', 'Content-Type':'application/json;charset=UTF-8'}
    # 设置请求头 - User-Agent | Content-Type
    # headers = {'User-Agent': ua, 'Content-Type':'application/json;charset=UTF-8'}
    # 设置请求头 - Content-Type
    # headers = {'Content-Type':'application/json;charset=UTF-8'}
    # 设置请求头 - Content-Type | Cookie
    headers = {'Content-Type':'application/json;charset=UTF-8', 'Cookie':'UM_distinctid=16b6de2813a19b-01a8b9731d6b64-3b7b516b-1aeaa0-16b6de2813bd10; Hm_lvt_b73e49f8578cedfcb3c39e6e8db9d782=1560916689; dtu session=9ca2ba75-f04d-421d-8f5c-4009a16bf528.9YnH2jAkLyMm9w3W3ZHJ4UPP6gM; Hm_lpvt_b73e49f8578cedfcb3c39e6e8db9d782=1561628377; remember_token=15519|8c07defb969a1233c94f3e14a5dbf0bb2b0ef9c4137bfafba3f93d39de1d56350be5c1b6b9dcf6a5b776270331eb627773e11a0c51db9bf7b1495b7d9256c22b'}
    # 设置cookies; 三种方式都行
    # 设置cookies - 使用dict初始化cookie的字典格式值
    # cookies = dict(UM_distinctid="16b6de2813a19b-01a8b9731d6b64-3b7b516b-1aeaa0-16b6de2813bd10", Hm_lvt_b73e49f8578cedfcb3c39e6e8db9d782="1560916689", isg="BDU14OPjhPyoU-BArDh_nT08UbcvGunicACBQrda_6z7jlWAfwOplEOH3RIdjgF8", dtu session="9ca2ba75-f04d-421d-8f5c-4009a16bf528.9YnH2jAkLyMm9w3W3ZHJ4UPP6gM", Hm_lpvt_b73e49f8578cedfcb3c39e6e8db9d782="1561628377", remember_token="15519|8c07defb969a1233c94f3e14a5dbf0bb2b0ef9c4137bfafba3f93d39de1d56350be5c1b6b9dcf6a5b776270331eb627773e11a0c51db9bf7b1495b7d9256c22b")
    # 设置cookies - 使用大括号{}初始化cookie的字典格式值
    # cookies = {"UM_distinctid":"16b6de2813a19b-01a8b9731d6b64-3b7b516b-1aeaa0-16b6de2813bd10", "Hm_lvt_b73e49f8578cedfcb3c39e6e8db9d782":"1560916689", "isg":"BDU14OPjhPyoU-BArDh_nT08UbcvGunicACBQrda_6z7jlWAfwOplEOH3RIdjgF8", "dtu session":"9ca2ba75-f04d-421d-8f5c-4009a16bf528.9YnH2jAkLyMm9w3W3ZHJ4UPP6gM", "Hm_lpvt_b73e49f8578cedfcb3c39e6e8db9d782":"1561628377", "remember_token":"15519|8c07defb969a1233c94f3e14a5dbf0bb2b0ef9c4137bfafba3f93d39de1d56350be5c1b6b9dcf6a5b776270331eb627773e11a0c51db9bf7b1495b7d9256c22b", "cna":"m3J7FeP9bCsCAXOrq2OjSoAW"}
    # 设置cookies - 在请求头中设置cookie的字符串值

    # 数据准备
    FormPostData = {"name":groupName, "parameter":{}}

    # 请求表单数据的三种方式 - 传递参数时：使用关键字参数允许函数调用时参数的顺序与声明时不一致
    # response = requests.post(url, cookies=cookies, data = json.dumps(FormPostData), headers = headers)
    # response = requests.post(url, data = json.dumps(FormPostData), headers = headers)
    response = requests.post(url, headers = headers, data = json.dumps(FormPostData))
    # 将Json格式字符串转为字典
    print(response.headers)
    # print(response.cookies)
    # print(response.cookies['dtu session'])
    # print(response.status_code)
    print(response.text)
    # print(json.loads(response.text))
    pass

if __name__ == "__main__":
    getPostTranslateData('leeprince0207')
