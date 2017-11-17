import time
from replyMsg import *
def replyXml(message):
    processFuns={"text":replyText,"image":replyImage,"location":replyLocation}
    if message.msgType in processFuns:
        response=processFuns[message.msgType](message).createXMlreply()
    return response


class Msg():
    def __init__(self,ToUserName='',FromUserName='',msg=None):
        if ToUserName and FromUserName:
            self.data = {}
            self.data['ToUserName'] = ToUserName
            self.data['FromUserName'] = FromUserName
            self.data['CreateTime'] = int(time.time())
        elif msg:
            self.data ={}
            self.data['ToUserName'] = msg.FromUserName
            self.data['FromUserName'] = msg.ToUserName
            self.data['CreateTime'] = int(time.time())

    def createXMlreply(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, ToUserName='',FromUserName='', msg=None, content):
        Msg.__init__(self,ToUserName=ToUserName,FromUserName=FromUserName,msg=msg)
        self.data['Content'] = content
    def createXMlreply(self):
        XmlTextForm = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[text]]></MsgType>
            <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlTextForm.format(**self.data)
    
class ImageMsg(Msg):
    def __init__(self,ToUserName='',FromUserName='',msg=None,MediaId):
        Msg.__init__(self,ToUserName=ToUserName,FromUserName=FromUserName,msg=msg)
        self.data['MediaId'] = MediaId
    def createXMlreply(self):
        XmlImageForm = """
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[image]]></MsgType>
            <Image>
                <MediaId><![CDATA[{MediaId}]]></MediaId>
            </Image>
        </xml>
        """
        return XmlImageForm.format(**self.data)

class MusicMsg(Msg):
    def __init__(self,ToUserName='',FromUserName='',msg=None,title,description,musicUrl,HQmusicUrl,MediaId='IJS0zz1EchXLLQE5JfGOu_hZJuTH0DjbPEQ4rDVIesQr3WLeTRKDlQn39xWnVEE_'):
        Msg.__init__(self,ToUserName=ToUserName,FromUserName=FromUserName,msg=msg)
        self.data['title']=title
        self.data['description']=description
        self.data['musicUrl']=musicUrl
        self.data['HQmusicUrl']=HQmusicUrl
        self.data['MediaId'] = MediaId
    def createXMlreply(self):
        XmlMusicForm="""
        <xml>
            <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
            <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
            <CreateTime>{CreateTime}</CreateTime>
            <MsgType><![CDATA[music]]></MsgType>
            <Music>
            <Title><![CDATA[{title}]]></Title>
            <Description><![CDATA[{description}]]></Description>
            <MusicUrl><![CDATA[{musicUrl}]]></MusicUrl>
            <HQMusicUrl><![CDATA[{HQmusicUrl}]]></HQMusicUrl>
            <ThumbMediaId><![CDATA[{MediaId}]]></ThumbMediaId>
            </Music>
        </xml>
        """
        return XmlMusicForm.format(**self.data)

    
