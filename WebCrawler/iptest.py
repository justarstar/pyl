# -*- coding: utf-8 -*-
 
#����requests��,û�а�װ �� cmd> pip install requests
import requests
 
#Ҫʹ�õĴ��� IP
#�����������ҵ�,�����˵Ļ��Լ��ҹ�
#����: https://www.xicidaili.com/
proxy = "175.42.123.205:9999"
#���ô���
proxies = {
    'http': 'http://' + proxy,      #����http���ӵ�
    'https': 'https://' + proxy,    #����https���ӵ�
}
#��������ͷ
User_Agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3"
headers = {'User-Agent': User_Agent}
try:
    #���,�����Զ��رն�������,��Ȼ���ױ� MaxRetryError
    s = requests.session()  #��ȡ �Ự
    s.keep_alive = False  #��������,��Ϊ false
    s.adapters.DEFAULT_RETRIES = 300  #������� ��Ϊ300
    #��ӡ����ͷ,������Ϣ
    print("headers",headers)
    print("proxies",proxies)
    #��������
    response = s.get( #���� s.get( �Ļ� ����ֱ���� requests.get(
            #���������ֱ�ӷ��������ַ,���Կ������IP
            "https://ifconfig.me/ip",
            proxies=proxies,
            headers=headers,
            timeout=5
    )
    #��ӡ��Ӧ����,����������IP�������ͳɹ���
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)