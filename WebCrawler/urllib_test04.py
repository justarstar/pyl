#-*-coding:GBK -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("http://fanyi.baidu.com/")
    response = request.urlopen(req)
    print("geturl��ӡ��Ϣ��%s"%(response.geturl()))
    print('**********************************************')
    print("info��ӡ��Ϣ��%s"%(response.info()))
    print('**********************************************')
    print("getcode��ӡ��Ϣ��%s"%(response.getcode()))