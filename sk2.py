from flask import Flask,render_template,request as request1
from urllib import request
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("sk1.html")
@app.route("/ajax")
def index1():
    url=request1.args.get("url")   #获取地址
    res=request.urlopen(url)       #通过地址打开目标返回一个http.client.HTTPResponse对象
    con=res.read().decode("utf8")  #.red读取里边的内容，内容为未解码   .decode解码
    return con

app.run()