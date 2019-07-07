# -*- coding: gbk -*-
from urllib import request
from urllib import parse
import json
 
if __name__ == "__main__":
	# ��Ӧ��ͼ��Request URL
	request_url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
	# ����Form Data�ֵ䣬�洢��ͼ�е�Form Data
	Form_Data = {}
	str = input("����������Ҫ��������ݣ�");
	Form_Data['i'] = str
	Form_Data['from'] = 'AUTO'
	Form_Data['to'] = 'AUTO'
	Form_Data['smartresult'] = 'dict'
	Form_Data['client'] = 'fanyideskweb'
	Form_Data['doctype'] = 'json'
	Form_Data['version'] = '2.1'
	Form_Data['keyfrom'] = 'fanyi.web'
	Form_Data['action'] = 'FY_BY_REALTIME'
	Form_Data['typoResult'] = 'false'
	# ʹ��urlencode����ת����׼��ʽ
	data = parse.urlencode(Form_Data).encode('utf-8')
	# ����Request�����ת�����ʽ������
	response = request.urlopen(request_url, data)
	# ��ȡ��Ϣ������
	html = response.read().decode('utf-8')
	# ʹ��json
	translate_results = json.loads(html)
	# �ҵ�������
	translate_result = translate_results["translateResult"][0][0]['tgt']
	# ��ӡ������
	print("����Ľ���� %s" % translate_result)