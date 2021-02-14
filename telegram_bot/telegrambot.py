import json
import string
import warnings
import intermediate
import requests
warnings.filterwarnings("ignore")

class telegram_bot():
    def __init__(self):
        self.token = "  <Token Value Goes Here"  
        self.url = f"https://api.telegram.org/bot{self.token}"
    def get_updates(self,offset=None):
        url = self.url+"/getUpdates?timeout=100"    
        if offset:
            url = url+f"&offset={offset+1}"
        url_info = requests.get(url)
        return json.loads(url_info.content)
    def send_message(self,msg,chat_id):
        url = self.url + f"/sendMessage?chat_id={chat_id}&text={msg}"
        if msg is not None:
            requests.get(url)
    def grab_token(self):
        return self.token
    
    
# main file 
tbot = telegram_bot()
update_id = None
def make_reply(msg):
    value = intermediate.reply(msg)
    return value
       
while True:
    print("...")
    updates = tbot.get_updates(offset=update_id)
    updates = updates['result']
    print(updates)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                try:
                    message = item["message"]["text"]
                    print("Message :", message)
                    from_ = item["message"]["from"]["id"]
                    reply = make_reply(message)
                    tbot.send_message(reply,from_)
                
                except:
                    message = item["edited_message"]["text"]
                    print("Message :", message)
                    from_ = item["edited_message"]["from"]["id"]
                    reply = make_reply(message)
                    tbot.send_message(reply,from_)
                
            except:              
                try:
                    message = None
                    from_ = item["message"]["from"]["id"]
                    print("ID: " , from_)
                    tbot.send_message("pardon?",from_)
                
                except:
                    message = None
                    from_ = item["edited_message"]["from"]["id"]
                    print("ID: " , from_)
                    tbot.send_message("pardon?",from_)
