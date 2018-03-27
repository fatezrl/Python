#linux py2
#-*- coding:utf-8 -*-
import requests
from PIL import  Image
from lxml import etree
import re
import os
from io import BytesIO
from bs4 import BeautifulSoup
import bs4
#from urllib import  parse
import urllib
import sys
reload(sys)
sys.setdefaultencoding('utf8')


'''
xingming =input('xingming')
xingming = parse.quote(xingming,'utf-8')
xingming = parse.quote(xingming,'utf-8')
'''
xuehao = raw_input('学号')
mima = raw_input('密码')



rs = requests.session()
r_1 = rs.get(url='http://hpuxzt.niool.com/index.php?s=/w0/LinianScore/LinianScore/index.html'
                             ,headers = {'Referer':'http://hpuxzt.niool.com/index.php?s=/w0/LinianScore/LinianScore/login/openid/o0Zy4wzytpe1-ulOhLhkRIV-qlFw.html'
                                         ,'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)'})
r_1.encoding=r_1.apparent_encoding
#print(r_1.encoding)
#print(r_1.text)

r_yzm = rs.get(url='http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2FCheckCode.aspx&b=0'
                                 , headers ={'Referer':'http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57&b=0&f=norefer'})
r_yzm_1= Image.open(BytesIO(r_yzm.content))

r_yzm_1.show()
r_yzm_1 = r_yzm_1.convert('RGB')
r_yzm_1.save('./yzm.jpg')
yzm = raw_input('输入验证码')
r_yzm_1.close()

r_post = rs.post(url='http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2Fdefault2.aspx&b=0',
                                 headers={'Referer':'http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57&b=0&f=norefer',
                                          "User-Agent": "Mozilla/5.0 "},
                                 data={'__VIEWSTATE':'dDwyODE2NTM0OTg7Oz7DQ76dY5N94xfdN2IRN0NxgHSm3Q==',
                                       'txtUserName':xuehao,
                                       'TextBox2':mima,
                                       'txtSecretCode':yzm ,
                                       'RadioButtonList1':'%D1%A7%C9%FA'
                                       ,'Button1':'',
                                       'lbLanguage':'',
                                       'hidPdrs':'',
                                       'hidsc':''})
r_post.encoding = r_post.apparent_encoding
#print(r_post.encoding )
#print(r_post.text)
soup3 = BeautifulSoup(r_post.text,'html.parser')
xingming_Post=soup3.find_all(id ='xhxm')
#print(xingming_Post)
for xm in xingming_Post:
    tds = xm.text

    s=tds

s__xm =s.strip('同学')

xingming =urllib.quote(s__xm,'utf-8')
#xingming = urllib.quote(xingming,'utf-8')



r_cjget = rs.get(url='http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2Fxscj_gc.aspx%3Fxh%3D'+xuehao+'%26xm%3D'+xingming+'%26gnmkdm%3DN121605&b=0'
                , headers={'Referer':'http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2Fxs_main.aspx%3Fxh%3D'+xuehao+'&b=0'})
soup = BeautifulSoup(r_cjget.content,'html.parser')
__VIEWSTATE = soup.input["value"]

r_cjpost = rs.post(url='http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2Fxscj_gc.aspx%3Fxh%3D'+xuehao+'%26amp%3Bxm%3D'+xingming+'%26amp%3Bgnmkdm%3DN121605&b=0',
                   headers= {'Referer':'http://wfkj1.papapoi.com/browse.php?u=http%3A%2F%2F202.196.225.57%2Fxscj_gc.aspx%3Fxh%3D'+xuehao+'%26xm%3D'+xingming+'%26gnmkdm%3DN121605&b=0'}
                  , data = {'__VIEWSTATE':__VIEWSTATE
                            ,'ddlXN':''
                            ,'ddlXQ':''
                            ,'Button1':'%B0%B4%D1%A7%C6%DA%B2%E9%D1%AF'
                            })






soup2 = BeautifulSoup(r_cjpost.text,'html.parser' ,from_encoding="gb2312")
#print(soup2)
#print(soup2.text)



def fillist(cjlist ):
    for tr in soup2.find('table').children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            cjlist.append([tds[3].string,tds[8].string])

ls =[]
fillist(ls)
#print(ls)
a = len(ls)
#print("{0:^12}\t{1:^13}\t".format("课程名称","分数",chr(12288)))
for i in range(len(ls)):
    u = ls[i]
    print("{0:^12}\t{1:^13}\t".format(u[0], u[1]), chr(12288))











