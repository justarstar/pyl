# -*- coding: gbk -*-
import requests,threading,datetime
from bs4 import BeautifulSoup
import random

'''
1��ץȡ���̴�����վ�Ĵ���ip
2��������ָ����Ŀ��url,��ץȡ��ip����Ч�Խ�����֤
3�����浽ָ����path
'''

# ------------------------------------------------------�ĵ�����--------------------------------------------------------
# д���ĵ�
def write(path,text):
    with open(path,'a', encoding='utf-8') as f:
        #writelines���԰��б��������д���ı��ļ��У��˴�����writeҲ����
        f.writelines(text)
        f.write('\n')
# ����ĵ�
def truncatefile(path):
    with open(path, 'w', encoding='utf-8') as f:
        #f.truncate(5)���ȡ���ļ���ͷ��5�ֽڴ�С�ĳ��ȣ�Ϊ�ջ�0size��ʾ����ļ�
        f.truncate()
# ��ȡ�ĵ�,�˴���ȡ�ĵ���Ҫ��Ϊ��ͳ����Чip�ĸ���
def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        txt = []
        for s in f.readlines():
            txt.append(s.strip())
    return txt
# ----------------------------------------------------------------------------------------------------------------------
# ����ʱ���,��ʽ: ʱ����
def gettimediff(start,end):
    #.seconds��ȡʱ�����ֵС��86400s��һ�������������.total_seconds������ʱ���
    seconds = (end - start).seconds
    #divmod��7,2���᷵�أ�3,1������7����2������3��������1
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    diff = ("%02d:%02d:%02d" % (h, m, s))
    return diff
# ----------------------------------------------------------------------------------------------------------------------
# ����һ�����������ͷ headers
def getheaders():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    UserAgent=random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers
# -----------------------------------------------------���ip�Ƿ����----------------------------------------------------
def checkip(targeturl,ip):
    headers =getheaders()  # ��������ͷ
    proxies = {"http": "http://"+ip, "https": "http://"+ip}  # ����ip
    try:
        response=requests.get(url=targeturl,proxies=proxies,headers=headers,timeout=5).status_code
        if response == 200 :
            return True
        else:
            return False
    except:
        return False

#-------------------------------------------------------��ȡ������----------------------------------------------------
# ��Ѵ��� XiciDaili
def findip(type,pagenum,targeturl,path): # ip����,ҳ��,Ŀ��url,���ip��·��
    list={'1': 'http://www.xicidaili.com/nt/', # xicidaili������ͨ����
          '2': 'http://www.xicidaili.com/nn/', # xicidaili���ڸ������
          '3': 'http://www.xicidaili.com/wn/', # xicidaili����https����
          '4': 'http://www.xicidaili.com/wt/'} # xicidaili����http����
    url=list[str(type)]+str(pagenum) # ����url
    headers = getheaders() # ��������ͷ
    html=requests.get(url=url,headers=headers,timeout = 5).text
    soup=BeautifulSoup(html,'lxml')
    all=soup.find_all('tr',class_='odd')
    for i in all:
        t=i.find_all('td')
        ip=t[1].text+':'+t[2].text
        is_avail = checkip(targeturl,ip)
        if is_avail == True:
            write(path=path,text=ip)
            print(ip)

#-----------------------------------------------------���߳�ץȡip���---------------------------------------------------
def getip(targeturl,path):
     truncatefile(path) # ��ȡǰ����ĵ�
     start = datetime.datetime.now() # ��ʼʱ��
     threads=[]
     for type in range(4):   # ��������ip,ÿ������ȡǰ��ҳ,��12���߳�
         for pagenum in range(3):
             t=threading.Thread(target=findip,args=(type+1,pagenum+1,targeturl,path))
             threads.append(t)
     print('��ʼ��ȡ����ip')
     for s in threads: # �������߳���ȡ
         s.start()
     for e in threads: # �ȴ������߳̽���
         e.join()
     print('��ȡ���')
     end = datetime.datetime.now() # ����ʱ��
     diff = gettimediff(start, end)  # �����ʱ
     ips = read(path)  # ��ȡ������ip����
     print('һ����ȡ����ip: %s ��,����ʱ: %s \n' % (len(ips), diff))

#-------------------------------------------------------����-----------------------------------------------------------
if __name__ == '__main__':
    path = 'iplist.txt' # �����ȡip���ĵ�path
    targeturl = 'http://redbrick.top/' # ��֤ip��Ч�Ե�ָ��url
    getip(targeturl,path)

