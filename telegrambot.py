from googlesearch import search 


import json
import string
import warnings
import requests
import nltkk
import searchmodule
warnings.filterwarnings("ignore")

class telegram_bot():
    def __init__(self):
        self.token = "1612346045:AAFiGHWYWr3rPhCdvQ8m6mTosVV4QxwofbA"  
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
    if(msg[0] == "/"):
        if(msg == "/start"):
            reply = "hey there, let's get started"
        elif("/search" in msg):
                reply1 = "sure!, here you go: "
                query =  msg
                print(query," is query")
                query = query.replace("/search","")
                print(query," is query")
                query = "https://www.iiitd.ac.in:" + query
                print(query," is query")
                for j in search(query, tld="co.in", num=1, stop=1, pause=2): 
                    print(j)
                    reply1 = reply1+j
                return reply1
        elif(msg == "/help"):
            reply = "have a look at our documentations"
        else:
            reply = "lemme have a look"
    elif msg == "heemank":
        reply = "yeah bro ?"
    else:
        #reply = "hey!"
        reply = nltkk.execute(msg)
    
    if(reply == None):
        reply = ""
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