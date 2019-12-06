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
    def is_going_to_onetotwo(self,event):
        text = event.message.text
        return text.lower() == "one to two"
    def is_going_to_onetothree(self,event):
        text = event.message.text
        return text.lower() == "one to three"
    def is_going_to_onetofour(self,event):
        text = event.message.text
        return text.lower() == "one to four"
    def is_going_to_onetofive(self,event):
        text = event.message.text
        return text.lower() == "one to five"
    
###
    def on_enter_advanced(self, event):
        
        reply_token = event.reply_token
        send_text_message(reply_token, "enter\n '12':from 1 to 2 lv \n '13':from 1 to 3 lv")
        #self.go_back()
##advanced ___
    def on_enter_onetotwo(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "60 Fragment of Memory")
        self.go_back_advanced()
    def on_enter_onetothree(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "60 Fragment of Memory")
        self.go_back_advanced()     
    def on_enter_onetofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "60 Fragment of Memory")
        self.go_back_advanced()
    def on_enter_onetofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "60 Fragment of Memory")
        self.go_back_advanced()
    def on_exit_onetotwo(self):
#
    def on_exit_advanced(self):
        print("Leaving advanced")

    def on_enter_showfunction(self, event):
        print("I'm entering showfunction")

        reply_token = event.reply_token
        send_text_message(reply_token, "'advanced':\n'help")
        self.go_back()
    #def on_exit_showfunction(self):
    def on_exit_state2(self):
        print("Leaving state2")
