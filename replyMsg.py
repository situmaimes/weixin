import replyXml
import re
def replyText(message):
    response=None
    if message.content=="录入信息":
        response=replyXml.TextMsg(msg=message,content="请按下列输入姓名学号生化成绩\n2016115448 杨靖康 87")
    if re.match(r"[\d]{10}[ ]*[\u4e00-\u9fa5]*[ ]*[\d\.]{2,4}",message.content):
        obj=re.search(r"([\d]{10})[ ]*([\u4e00-\u9fa5]*)[ ]*([\d\.]{2,4})",message.content)
        name=obj[2]
        id=obj[1]
        bioChem=obj[3]
        print(name,id,bioChem)
        response=replyXml.TextMsg(msg=message,content="成功")
#    else:
#        content=message.content[::-1]
#        response=replyXml.TextMsg(msg=message,content=content)
    return response or replyXml.TextMsg(msg=message,content="sorry i don't like you")


def replyImage(message):
    response=replyXml.ImageMsg(msg=message,MediaId=message.MediaId)
    return response
def replyLocation(message):
    title="Nyan Cat"
    description="喵喵喵"
    musicUrl="""http://m10.music.126.net/20171021161209/32b3cc036c723b0cfde77c4f42082d3b/ymusic/8658/1544/89b9/56b00498b351e90df685a5351ac3df33.mp3"""
    HQmusicUrl=musicUrl
    response=replyXml.MusicMsg(msg=message,title=title,description=description,musicUrl=musicUrl,HQmusicUrl=HQmusicUrl)
    return response
