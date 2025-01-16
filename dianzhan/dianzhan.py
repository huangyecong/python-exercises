# python 实现一个简单点赞系统

from flask import Flask,render_template,request
data = [
  {'id':0,'name':'中秋节','num':0},
  {'id':1,'name':'春节','num':0},
  {'id':2,'name':'端午节','num':0},
]
app = Flask(__name__)
@app.route('/index')
def index():
  return render_template('index.html',data=data)

@app.route('/dianzhan')
def dianzhan():
  id = request.args.get('id')
  data[int(id)]['num'] += 1
  return render_template('index.html',data=data)

app.run(debug=True)