import xml.etree.ElementTree as ET

def parse(data):
    if len(data) == 0:
        return None
    xmlData = ET.fromstring(data)
    msgType=xmlData.find('MsgType').text
    if msgType=='text':
        return TextXml(xmlData)
    elif msgType=='image':
        return ImageXml(xmlData)
    elif msgType=='location':
        return NormalLocationXml(xmlData)
    else:
        return None

class Xml():
    def __init__(self, xmlData):
        self.xmlData=xmlData
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.XmlType = xmlData.find('MsgType').text

class NormalXml(Xml):
    def __init__(self,xmlData):
        Xml.__init__(self, xmlData)
        self.XmlId=xmlData.find('MsgId').text

class TextXml(NormalXml):
    def __init__(self,xmlData):
        NormalXml.__init__(self, xmlData)
        self.content=xmlData.find('Content').text
        
class ImageXml(NormalXml):
    def __init__(self,xmlData):
        NormalXml.__init__(self, xmlData)
        self.PicUrl=xmlData.find('PicUrl').text
        self.MediaId = xmlData.find('MediaId').text

class NormalLocationXml(NormalXml):
    def __init__(self,xmlData):
        NormalXml.__init__(self,xmlData)
        self.Location_X = xmlData.find("Location_X").text
        self.Location_Y = xmlData.find("Location_Y").text
        self.Scale=xmlData.find("Scale").text
        self.Label=xmlData.find("Label").text
  

# class EventXml(Xml):
#     def _init__(self,xmlData):
#         Xml.__init__(self,xmlData)
#         self.Event = xmlData.find('Event').text

# class ClickXml(EventXml):
#     def __init__(self,xmlData):
#         EventXml.__init__(self,xmlData)
#         self.Eventkey = xmlData.find('EventKey').text

# class SubscribeXml(EventXml):
#     def __init__(self,xmlData):
#         EventXml.__init__(self,xmlData)

# class UnsubscribeXml(EventXml):
#     def __init__(self,xmlData):
#         EventXml.__init__(self,xmlData)

# class ViewXml(EventXml):
#     def __init__(self,xmlData):
#         EventXml.__init__(self,xmlData)
#         self.EventKey=xmlData.find('EventKey').text
# class LocationXml(EventXml):
#     def __init__(self,xmlData):
#         EventXml.__init__(self,xmlData)
#         self.Latitude=xmlData.find("Latitude").text
#         self.Longitude=xmlData.find("Longitude").text
#         self.Precision=xmlData.find("Precision").text
