from mycroft import MycroftSkill, intent_file_handler


class Horoscope(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('horoscope.intent')
    def handle_horoscope(self, message):
        sign = message.data.get('sign')
        horoscope = ''

        self.speak_dialog('horoscope', data={
            'horoscope': horoscope,
            'sign': sign
        })


def create_skill():
    return Horoscope()

