from mycroft import MycroftSkill, intent_file_handler
import urllib, urllib.request, json, re
from urllib.request import Request

class Horoscope(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('horoscope.intent')
    def handle_horoscope(self, message):
        sign = message.data['sign']
        apiUrl = "http://sandipbgt.com/theastrologer/api/horoscope/%s/today/" %sign
        text = urllib.request.urlopen(apiUrl).read()
        full_resp = json.loads(text)
        final_horo = full_resp["horoscope"].split("(c)")[0]
        
        # self.speak_dialog('horoscope', {'horoscope':final_horo})


        
        # sign = message.data.get('sign')
        # horoscope = ''

        self.speak_dialog(final_horo)


def create_skill():
    return Horoscope()



