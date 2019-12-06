from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
#1
    def is_going_to_advanced(self, event):
        text = event.message.text
        return text.lower() == "advanced"
#2
    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"
#3
    def is_going_to_showfunction(self,event):
        text = event.message.text
        return text.lower() == "help"
###
    def on_enter_advanced(self, event):
        print("I'm entering advanced")

        reply_token = event.reply_token
        send_text_message(reply_token, "enter '12'
                          '13'")
       
        self.go_back()

    def on_exit_advanced(self):
        print("Leaving advanced")

    def on_enter_showfunction(self, event):
        print("I'm entering showfunction")

        reply_token = event.reply_token
        send_text_message(reply_token, "'advanced':
'help'")
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")
