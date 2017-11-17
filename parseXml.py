import xml.etree.ElementTree as ET

def parseXml(data):
    if len(data) == 0:
        return None
    xmlData = ET.fromstring(data)
    processClasses={"text":TextMsg,'image':ImageMsg,"location":NormalLocationMsg}
    processClass=processClasses.get(xmlData.find('MsgType').text)
    if processClass:
        return processClass(xmlData)
    else:
        return None


class Msg():
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text

class NormalMsg(Msg):
    def __init__(self,xmlData):
        Msg.__init__(self, xmlData)
        self.MsgId=xmlData.find('MsgId').text

class TextMsg(NormalMsg):
    def __init__(self,xmlData):
        NormalMsg.__init__(self, xmlData)
        self.content=xmlData.find('Content').text
        
class ImageMsg(NormalMsg):
    def __init__(self,xmlData):
        NormalMsg.__init__(self, xmlData)
        self.PicUrl=xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class NormalLocationMsg(NormalMsg):
    def __init__(self,xmlData):
        NormalMsg.__init__(self,xmlData)
        self.Location_X = xmlData.find("Location_X").text
        self.Location_Y = xmlData.find("Location_Y").text
        self.Scale=xmlData.find("Scale").text
        self.Label=xmlData.find("Label").text

