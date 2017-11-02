import time
from parseXml import *
#from chat import chat

def reply(one):
    print(one)
    if not one:
        two=Msg()
    else:
        if isinstance(one,TextXml):
            if one.content.strip().lower()=="music":
                title="Nyan Cat"
                description="喵喵喵"
                musicUrl="""http://m10.music.126.net/20171021161209/32b3cc036c723b0cfde77c4f42082d3b/ymusic/8658/1544/89b9/56b00498b351e90df685a5351ac3df33.mp3"""
                HQmusicUrl=musicUrl
                two=MusicMsg(one,title=title,description=description,musicUrl=musicUrl,HQmusicUrl=HQmusicUrl)
            else:
                #content=chat(one.content)
                content=one.content[::-1]
                two=TextMsg(one,content)
        elif isinstance(one,ImageXml):
            two=ImageMsg(one,one.MediaId)
        elif isinstance(one,NormalLocationXml):
            content=' '.join([one.Label,one.Location_X,one.Location_Y])
            two=TextMsg(one,content)
        else:
            two=Msg(one)
        print(two)
        return two

class Msg():
    def __init__(self,one=''):
        if one:
            self.data = {}
            self.data['ToUserName'] = one.FromUserName
            self.data['FromUserName'] = one.ToUserName
            self.data['CreateTime'] = int(time.time())
    def send(self):
        return "success"

class TextMsg(Msg):
    def __init__(self, one, content):
        Msg.__init__(self,one)
        self.data['Content'] = content
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
        return XmlTextForm.format(**self.data)
    
class ImageMsg(Msg):
    def __init__(self,one,MediaId):
        Msg.__init__(self,one)
        self.data['MediaId'] = MediaId
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
        return XmlImageForm.format(**self.data)

class MusicMsg(Msg):
    def __init__(self,one,title,description,musicUrl,HQmusicUrl,MediaId='IJS0zz1EchXLLQE5JfGOu_hZJuTH0DjbPEQ4rDVIesQr3WLeTRKDlQn39xWnVEE_'):
        Msg.__init__(self,one)
        self.data['title']=title
        self.data['description']=description
        self.data['musicUrl']=musicUrl
        self.data['HQmusicUrl']=HQmusicUrl
        self.data['MediaId'] = MediaId
    def send(self):
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

    
