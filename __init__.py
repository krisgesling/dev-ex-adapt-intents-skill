from mycroft import MycroftSkill, intent_file_handler


class DevExAdaptIntents(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('intents.adapt.ex.dev.intent')
    def handle_intents_adapt_ex_dev(self, message):
        self.speak_dialog('intents.adapt.ex.dev')


def create_skill():
    return DevExAdaptIntents()

