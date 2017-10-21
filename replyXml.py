import time
from parseXml import *
#from chat import chat

def reply(one):
    if not one:
        two=Msg()
    else:
        if isinstance(one,TextXml):
            if one.content.strip().lower()=="music":
                title="Nyan Cat"
                description="喵喵喵"
                musicUrl="""http://m10.music.126.net/20171021161209/32b3cc036c723b0cfde77c4f42082d3b/ymusic/8658/1544/89b9/56b00498b351e90df685a5351ac3df33.mp3"""
                HQmusicUrl=musicUrl
                MediaId=''
                two=MusicMsg(one,title=title,description=description,musicUrl=musicUrl,HQmusicUrl=HQmusicUrl,MediaId=MediaId)
            else:
                #content=chat(one.content)
                content=one.content[::-1]
                two=TextMsg(one,content)
        elif isinstance(one,ImageMsg):
            two=ImageMsg(one,one.MediaId)
        elif isinstance(one,NormalLocationXml):
            content=' '.join[one.Label,one.Location_X,one.Location_Y]
            two=TextMsg(one,content)
        else:
            two=Msg(one)
        return two

class Msg():
    def __init__(self,one=''):
        if not one:
            self.__dict = dict()
            self.__dict['ToUserName'] = one.ToUserName
            self.__dict['FromUserName'] = one.FromUserName
            self.__dict['CreateTime'] = int(time.time())
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, one, content):
        Msg.__init__(self,one)
        self.__dict['Content'] = content
    def send(self):
        XmlTextForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlTextForm.format(**self.__dict)
    
class ImageMsg(Msg):
    def __init__(self,one,MediaId):
        Msg.__init__(self,one)
        self.__dict['MediaId'] = MediaId
    def send(self):
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
        return XmlImageForm.format(**self.__dict)

class MusicMsg(Msg):
    def __init__(self,one,title,description,musicUrl,HQmusicUrl,MediaId):
        Msg.__init__(self,one)
        self.__dict['title']=title.encode()
        self.__dict['description']=description.encode()
        self.__dict['musicUrl']=musicUrl.encode()
        self.__dict['HQmusicUrl']=HQmusicUrl.encode()
        self.__dict['MediaId'] = MediaId
    def send(self):
        XmlMusicForm="""
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[music]]></MsgType>
        <Music>
        <Title><![CDATA[{title}]></Title>
        <Description><![CDATA[{description}]]></Description>
        <MusicUrl><![CDATA[{musicUrl}]]></MusicUrl>
        <HQMusicUrl><![CDATA[{HQmusicUrl}]]></HQMusicUrl>
        <ThumbMediaId><![CDATA[{MediaId}]]></ThumbMediaId>
        </Music>
        </xml>
        """
        return XmlMusicForm.format(**self.__dict)

    
