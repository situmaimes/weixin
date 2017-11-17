"""
author:situmaimes
2017.10.15 1.0 自动倒序回复
2017.11.17 1.01 自动录入信息,重新设计架构更易扩展
"""


import hashlib
from flask import Flask, request
from parseXml import parseXml
from replyXml import replyXml
app = Flask(__name__)
app.debug = True

@app.route('/weixin', methods=['GET', 'POST'])
def weChat():
    if request.method == 'GET':
        token = 'Yangjingkang' 
        signature = request.args.get('signature', '')
        timestamp = request.args.get('timestamp', '')
        nonce = request.args.get('nonce', '')
        echostr = request.args.get('echostr', '')
        s = ''.join(sorted([timestamp, nonce, token]))
        if hashlib.sha1(s.encode()).hexdigest() == signature:
            return echostr
    else:
        _msg=parseXml(request.data)
        if _msg:
            print("get a message from ",_msg.FromUserName)
            return replyXml(_msg)
        else:
            return "success"


        
@app.route('/')
def hello():
    return 'hello,everybody./nMy name is Yang Jing Kang./nBye!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
