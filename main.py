import hashlib
from flask import Flask, request
from parseXml import parse
from replyXml import reply
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
        one=parse(request.data)
        print("处理成功",one)
        data=reply(one).send()
        print(data)
        return data
  
 
        
@app.route('/')
def hello():
    return 'hello,everybody./nMy name is Yang Jing Kang./nBye!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
