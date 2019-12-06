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
    #advanced
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
    def is_going_to_twotothree(self,event):
        text = event.message.text
        return text.lower() == "two to three"
    def is_going_to_twotofour(self,event):
        text = event.message.text
        return text.lower() == "two to four"
    def is_going_to_twotofive(self,event):
        text = event.message.text
        return text.lower() == "two to five"
    def is_going_to_threetofive(self,event):
        text = event.message.text
        return text.lower() == "three to four"
    def is_going_to_threetofive(self,event):
        text = event.message.text
        return text.lower() == "three to five"
    def is_going_to_fourtofive(self,event):
        text = event.message.text
        return text.lower() == "four to five"
    ##advinced
    def is_going_to_user(self,event):
        text = event.message.text
        return text.lower() == "initial"
#
    def on_enter_advanced(self, event):
        
        reply_token = event.reply_token
        send_text_message(reply_token, "enter\n '12':from 1 to 2 lv \n '13':from 1 to 3 lv")
        #self.go_back()
    def on_enter_user(self, event):
        
        reply_token = event.reply_token
        send_text_message(reply_token, "initial")

#advanced ___
    def on_enter_onetotwo(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "60 女神的秘石 或 30 記憶碎片")
        self.go_back_advanced()
        
    def on_enter_onetothree(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "260 女神的秘石 或 130 記憶碎片")
        self.go_back_advanced()
        
    def on_enter_onetofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "500 女神的秘石 或 250 記憶碎片")
        self.go_back_advanced()
        
    def on_enter_onetofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "800 女神的秘石 或 400 記憶碎片")
        self.go_back_advanced()
    #2-345
    def on_enter_twotothree(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "200 女神的秘石 或 100 記憶碎片")
        self.go_back_advanced()
    def on_enter_twotofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "440 女神的秘石 或 220 記憶碎片")
        self.go_back_advanced()
    def on_enter_twotofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "740 女神的秘石 或 370 記憶碎片")
        self.go_back_advanced()
    def on_enter_threetofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "240 女神的秘石 或 120 記憶碎片")
        self.go_back_advanced()
    def on_enter_threetofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "300 女神的秘石 或 150 記憶碎片")
        self.go_back_advanced()
    def on_enter_fourtofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "540 女神的秘石 或 270 記憶碎片")
        self.go_back_advanced()
    #
    #def on_exit_advanced(self):
    #    print("Leaving advanced")

    def on_enter_showfunction(self, event):
        print("I'm entering showfunction")

        reply_token = event.reply_token
        send_text_message(reply_token, "'advanced':\n'help")
        self.go_back()
        
    #def on_exit_showfunction(self):
    #def on_exit_state2(self):
     #   print("Leaving state2")
