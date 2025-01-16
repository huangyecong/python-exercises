#python制作一个查询工具练习

#pip install requests
import requests
#pip install lxml
from lxml import etree
#pip install flask
from flask import Flask,render_template,request
app = Flask(__name__)


# ------------------------------------------查手机方法
def get_mobile(phone):
  #发送请求的链接
  url = f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
  
  #伪装自己
  headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
  }

  # 发送请求
  resq = requests.get(url,headers=headers)

  # 设置中文显示
  resq.encoding = 'utf-8'

  #解析数据
  e = etree.HTML(resq.text)

  # 编写xPath提取数据
  datas = e.xpath('//tr/td[2]/a[1]/text()')
  
  # 响应数据
  return datas

# ------------------------------------------显示数据
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search_phone')
def search_phone():
  # 注意这里的request，没有s
  phone = request.args.get('phone')
  result = get_mobile(phone)
  return '<br/>'.join(result)
  
app.run(debug=True)