import json
import string
import warnings
import requests
warnings.filterwarnings("ignore")

class telegram_bot():
    def __init__(self):
        self.token = "1641823012:AAEqUcEKo3_3XuN-o2ST1TGwXrH8M2N8dsc"  
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
    reply = None
    if msg == "heemank":
        reply = "yeah bro ?"
    elif msg is not None:
        reply1 = "Currently under construction: "
        reply2 = input("Enter a personalized message for user: ")
        reply =reply1 + reply2
    return reply
       
while True:
    print("...")
    updates = tbot.get_updates(offset=update_id)
    updates = updates['result']
    print(updates)
    if updates:
        for item in updates:
            update_id = item["update_id"]
            print(update_id)
            try:
                message = item["message"]["text"]
                print("Message :", message)
            except:
                print("Message :", None)

            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            tbot.send_message(reply,from_)
            
            


