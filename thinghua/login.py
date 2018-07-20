#获取学生课程信息
#coding:utf-8
import requests
import json
from PIL import Image
from io import BytesIO

def printinfo(a):
    print(a.status_code)
    a.encoding = a.apparent_encoding
    print(a.text)
rs =requests.session()
xuehao = input('学号')
mima = input('密码')
#登录学号密码
rp_id =rs.post(url='http://sso.tsinghuawaiyu.com/v1/tickets',
            headers={


                    'Content-Length': '41',

                    'Host': 'sso.tsinghuawaiyu.com',

                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept':'*/*',
                    'Accept-Language': 'zh-CN',
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                    'Referer': 'http://sso.tsinghuawaiyu.com/v1/tickets',

            },
            data={
                'username':xuehao,
                'password' :mima
            })
longin =json.loads(rp_id.text)['result']['msg']
if str(longin) =='用户名密码错误!':
    print(longin)
else:
    #生成st
    rp_st =rs.post(url='http://sso.tsinghuawaiyu.com/v1/serviceTicket',
            headers={


                    'Content-Length': '63',

                    'Host': 'sso.tsinghuawaiyu.com',

                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept':'*/*',
                    'Accept-Language': 'zh-CN',
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                    'Referer': 'http://sso.tsinghuawaiyu.com/v1/serviceTicket',

            },
            data={
                'service':'http://school.tsinghuawaiyu.com/client/user/currentuser',

            })
    st =json.loads(rp_st.text)['data']['serverTicket']
    print(st)

#jessionid BY st




#uuid  name school BY st

    rg_uuid = rs.get(url='http://school.tsinghuawaiyu.com/client/user/currentuser?ticket='+str(st),
            headers={




                    'Host': 'school.tsinghuawaiyu.com',

                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept':'*/*',
                    'Accept-Language': 'zh-CN',
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                    'Referer': 'school.tsinghuawaiyu.com/client/user/currentuser?ticket='+str(st),

            },
           )
    uuid =json.loads(rg_uuid.text)['data']['uuid']
    realname =json.loads(rg_uuid.text)['data']['realname']
    schoolname =json.loads(rg_uuid.text)['data']['organName']
    username =json.loads(rg_uuid.text)['data']['username']
#teachername crouses BY jessionid
    rp_nc =rs.post(url='http://school.tsinghuawaiyu.com/client/course/list-of-student?status=1&pager.pageSize=8',
            headers={


                    'Content-Length': '37',

                    'Host': 'school.tsinghuawaiyu.com',

                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept':'*/*',
                    'Accept-Language': 'zh-CN',
                    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                    'Referer': 'http://school.tsinghuawaiyu.com/client/course/list-of-student?status=1&pager.pageSize=8',

            },
            data={
                'username':xuehao,
                'password' :mima
            })
    crousrslist=json.loads(rp_nc.text)['data']['list']
    for each in crousrslist:
        print(each['courseName'])
        print(each['lecturerName'])
    print(username)
    print(schoolname)
    print(realname)
    printinfo(rp_id)






