# -*- coding: gbk -*-
# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    #������ַ
    url = 'https://ifconfig.me/ip'
    #���Ǵ���IP
	
    proxy = {'https':'175.42.123.205:9999'}
    #����ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #����Opener
    opener = request.build_opener(proxy_support)
    #���User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #��װOPener
    request.install_opener(opener)
    #ʹ���Լ���װ�õ�Opener
    response = request.urlopen(url)
    #��ȡ��Ӧ��Ϣ������
    html = response.read().decode("utf-8")
    #��ӡ��Ϣ
    print(html)