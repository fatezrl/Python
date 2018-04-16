#coding:utf-8
# coding:utf-8
# coding:utf-8
# ojbk
from flask import Flask, request, render_template,abort
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import pytesseract
import PIL.ImageOps
import re

app = Flask(__name__)

def initTable(threshold=140):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    return table



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/', methods=["POST"])
def index_post():
    rs = requests.session()
    rs_get = rs.get(url=' http://218.196.240.97/loginAction.do'
                    , headers={'Referer': 'http://218.196.240.97/'
            , 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'})
    r_yzm = rs.get(url='http://218.196.240.97/validateCodeAction.do'
                   , headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              })
    r_yzm_1 = Image.open(BytesIO(r_yzm.content))

    im = r_yzm_1.convert('L')

    binaryImage = im.point(initTable(), '1')

    im1 = binaryImage.convert('L')
    im2 = PIL.ImageOps.invert(im1)
    im3 = im2.convert('1')
    im4 = im3.convert('L')
    # 将图片中字符裁剪保留
    # box = (30, 10, 90, 28)
    # region = im4.crop(box)
    # 将图片字符放大
    out = im4.resize((120, 40))
    code = pytesseract.image_to_string(im)
    # code = pytesseract.image_to_string(r_yzm_1)
    yzm = str(code)
    yzm = yzm.replace(' ', '')
    yzm = re.sub('[^A-Za-z0-9]', '', yzm)
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    print(yzm)
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    xuehao = request.form.get('xuehao')
    mima = request.form.get('mima')

    r_post = rs.post(url='http://218.196.240.97/loginAction.do',
                     headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0 "},
                     data={
                         'zjh': xuehao,
                         'mm': mima,
                         'v_yzm': yzm,

                     })
    r_post.encoding = r_post.apparent_encoding
    # print(r_post.links)
    # print(rs_get.cookies)
    # print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    # print(r_post.cookies)
    # print(r_post.content)
    # print(r_post.next)

    r_cjpost = rs.post(url=' http://218.196.240.97/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001', )
    r_cjpost.encoding = r_cjpost.apparent_encoding
    # print(r_cjpost.text)
    soup2 = BeautifulSoup(r_cjpost.text, 'html.parser')
    return str(soup2)


@app.errorhandler(500)
def page_not_found(error):
    rs_2 = requests.session()
    rs_get = rs_2.get(url=' http://218.196.240.97/loginAction.do'
                    , headers={'Referer': 'http://218.196.240.97/'
            , 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'})
    r_yzm_2 = rs_2.get(url='http://218.196.240.97/validateCodeAction.do'
                   , headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              })
    r_yzm_1_2 = Image.open(BytesIO(r_yzm_2.content))

    im_2 = r_yzm_1_2.convert('L')

    binaryImage = im_2.point(initTable(), '1')

    im1 = binaryImage.convert('L')
    im2 = PIL.ImageOps.invert(im1)
    im3 = im2.convert('1')
    im4 = im3.convert('L')
    # 将图片中字符裁剪保留
    # box = (30, 10, 90, 28)
    # region = im4.crop(box)
    # 将图片字符放大
    out = im4.resize((120, 38))
    code_2 = pytesseract.image_to_string(out)
    # code = pytesseract.image_to_string(r_yzm_1)
    yzm_2 = str(code_2)
    yzm_2 = yzm_2.replace(' ', '')
    yzm_2 = re.sub('[^A-Za-z0-9]', '', yzm_2)
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    print(yzm_2)
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    xuehao_2 = request.form.get('xuehao')
    mima_2 = request.form.get('mima')

    r_post_2 = rs_2.post(url='http://218.196.240.97/loginAction.do',
                     headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0 "},
                     data={
                         'zjh': xuehao_2,
                         'mm': mima_2,
                         'v_yzm': yzm_2,

                     })
    r_post_2.encoding = r_post_2.apparent_encoding
    # print(r_post.links)
    # print(rs_get.cookies)
    # print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    # print(r_post.cookies)
    # print(r_post.content)
    # print(r_post.next)

    r_cjpost_2 = rs_2.post(url=' http://218.196.240.97/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001', )
    r_cjpost_2.encoding = r_cjpost_2.apparent_encoding
    # print(r_cjpost.text)
    if r_cjpost_2.status_code == 200:
        soup2_2 = BeautifulSoup(r_cjpost_2.text, 'html.parser')

        return str(soup2_2)
    else:
        abort(403)


@app.errorhandler(403)
def page_not_found_104(error2):
    rs_2 = requests.session()
    rs_get = rs_2.get(url=' http://218.196.240.97/loginAction.do'
                    , headers={'Referer': 'http://218.196.240.97/'
            , 'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'})
    r_yzm_2 = rs_2.get(url='http://218.196.240.97/validateCodeAction.do'
                   , headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              })
    r_yzm_1_2 = Image.open(BytesIO(r_yzm_2.content))

    im_2 = r_yzm_1_2.convert('L')

    binaryImage = im_2.point(initTable(), '1')

    im1 = binaryImage.convert('L')
    im2 = PIL.ImageOps.invert(im1)
    im3 = im2.convert('1')
    im4 = im3.convert('L')
    # 将图片中字符裁剪保留
    # box = (30, 10, 90, 28)
    # region = im4.crop(box)
    # 将图片字符放大
    out = im4.resize((120, 38))
    code_2 = pytesseract.image_to_string(out)
    # code = pytesseract.image_to_string(r_yzm_1)
    yzm_2 = str(code_2)
    yzm_2 = yzm_2.replace(' ', '')
    yzm_2 = re.sub('[^A-Za-z0-9]', '', yzm_2)

    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    print(yzm_2)
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    xuehao_2 = request.form.get('xuehao')
    mima_2 = request.form.get('mima')

    r_post_2 = rs_2.post(url='http://218.196.240.97/loginAction.do',
                     headers={'Referer': 'http://218.196.240.97/loginAction.do',
                              "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0 "},
                     data={
                         'zjh': xuehao_2,
                         'mm': mima_2,
                         'v_yzm': yzm_2,

                     })
    r_post_2.encoding = r_post_2.apparent_encoding
    # print(r_post.links)
    # print(rs_get.cookies)
    # print('1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    # print(r_post.cookies)
    # print(r_post.content)
    # print(r_post.next)

    r_cjpost_2 = rs_2.post(url=' http://218.196.240.97/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001', )
    r_cjpost_2.encoding = r_cjpost_2.apparent_encoding
    # print(r_cjpost.text)
    soup2_2 = BeautifulSoup(r_cjpost_2.text, 'html.parser')
    #return str(soup2_2)
    if r_cjpost_2.status_code == 200:
        #soup2_2 = BeautifulSoup(r_cjpost_2.text, 'html.parser')

        return str(soup2_2)
    else:
        abort(400)
@app.errorhandler(400)
def index_40000(a):
    return '请输入正确的信息并重试'




if __name__ == '__main__':
    # app.run(threaded=True)
    # app.run(tr)
    app.run(host="0.0.0.0", port=5000, threaded=True,)

'''

服务器已经接收成绩

尝试客户端接收数据
验证码识别率低
已优化图片处理机制


异常处理不完善

'''

