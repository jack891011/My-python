# -*- coding: utf-8 -*-
from urllib import request
import re,simplejson

def checkip(ip):
    s=request.urlopen('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=%s' % ip)
    d=simplejson.load(s)
    print(d['country'], d['province'], d['city'])
    return(d['country'],d['province'],d['city'])



def authlogcheck(filepath):
    with open(filepath,'r') as f :
        for a in f.readlines():
            if len(re.findall(r'Accepted\s+(password|publickey)',a)) > 0:
                ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',a)
                try:
                    checkip(ip[0])
                except:
                    pass

if __name__=='__main__':
    a=input('输入文件名或者IP地址:')
    if re.match(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})',a):
        try:
            checkip(a)
        except:
            raise 'IP格式有误'
    else:
        try:
            authlogcheck(a)
        except:
            print('请输入正确的文件路径')
