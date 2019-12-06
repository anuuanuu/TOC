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
    
    #def is_going_to_references(self,event):
     #   text = event.message.text
    #    return text.lower() == "references"
    
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
    def is_going_to_threetofour(self,event):
        text = event.message.text
        return text.lower() == "three to four"
    def is_going_to_threetofive(self,event):
        text = event.message.text
        return text.lower() == "three to five"
    def is_going_to_fourtofive(self,event):
        text = event.message.text
        return text.lower() == "four to five"
    ##advinced
    ##references
    def is_going_to_references(self,event):
        text = event.message.text
        return text.lower() == "references"
    def is_going_to_mana(self,event):
        text = event.message.text
        return text.lower() == "mana"
    def is_going_to_stamina(self,event):
        text = event.message.text
        return text.lower() == "stamina"
    def is_going_to_exp(self,event):
        text = event.message.text
        return text.lower() == "exp"
    #def on_enter_references(self, event):
     #   reply_token = event.reply_token
    #    send_text_message(reply_token, "'mana'")
   #     self.go_back()
    def on_enter_mana(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://pcredivewiki.tw/Other/Mana")
        self.go_back()
    def on_enter_stamina(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://pcredivewiki.tw/Other/Stamina")
        self.go_back()
    def on_enter_exp(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "https://pcredivewiki.tw/Other/Exp")
        self.go_back()
      
    ##references
    def is_going_to_user(self,event):
        text = event.message.text
        return text.lower() == "initial"
#
    def on_enter_advanced(self, event):
        
        reply_token = event.reply_token
        send_text_message(reply_token, "enter n to m\n  n<m \n ex:one to two\n 從n星升到m星")
        #self.go_back()
    def on_enter_user(self, event):
        
        reply_token = event.reply_token
        send_text_message(reply_token, "initial")

#advanced ___
    def on_enter_onetotwo(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 60 女神的秘石 或 30 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
        
    def on_enter_onetothree(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 260 女神的秘石 或 130 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
        
    def on_enter_onetofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 500 女神的秘石 或 250 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
        
    def on_enter_onetofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 800 女神的秘石 或 400 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    #2-345
    def on_enter_twotothree(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 200 女神的秘石 或 100 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    def on_enter_twotofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 440 女神的秘石 或 220 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    def on_enter_twotofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 740 女神的秘石 或 370 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    def on_enter_threetofour(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 240 女神的秘石 或 120 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    def on_enter_threetofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 300 女神的秘石 或 150 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    def on_enter_fourtofive(self,event):
        reply_token = event.reply_token
        send_text_message(reply_token, "需要 540 女神的秘石 或 270 記憶碎片\n enter n to m\n  n<m \n ex:one to two\n 從n星升到m星\n or enter 'initial':return menu")
        self.go_back_advanced()
    #
    #def on_exit_advanced(self):
    #    print("Leaving advanced")

    def on_enter_showfunction(self, event):
        print("I'm entering showfunction")

        reply_token = event.reply_token
        send_text_message(reply_token, "'advanced':升星所需材料\n'help':查詢指令\n''")
        self.go_back()
    
    def on_enter_references(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "'mana':技能等級花費瑪娜\n'stamina':體力計算\n'exp':角色所需經驗")
        self.go_back()
    #def on_exit_showfunction(self):
    #def on_exit_state2(self):
     #   print("Leaving state2")
