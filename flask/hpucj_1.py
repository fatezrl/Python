#coding:utf-8
from flask import Flask, request, render_template,abort
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import pytesseract
import PIL.ImageOps
import re
import time

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
    c = 201
    while(c !=200):
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
        #yzm = re.sub('[^A-Za-z0-9]', '', yzm)
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
        a = time.time()
        try:
            r_cjpost = rs.post(url=' http://218.196.240.97/gradeLnAllAction.do?type=ln&oper=sxinfo&lnsxdm=001', timeout =2)
            b =time.time()
            print(b-a)
            r_cjpost.encoding = r_cjpost.apparent_encoding
            # print(r_cjpost.text)
            c =r_cjpost.status_code
            soup2 = BeautifulSoup(r_cjpost.text, 'html.parser')
            return str(soup2)
        except:
            c = 201
@app.errorhandler(500)
def page_not_found(error):
    return "请输入正确的密码"

if __name__ == '__main__':

    app.run(host="0.0.0.0", port=5000, threaded=True,)



