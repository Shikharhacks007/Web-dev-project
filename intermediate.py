import nltkk
import searchmodule
from googlesearch import search 

def reply(msg):
    if(msg[0] == "/"):
        if(msg == "/start"):
            reply = "hey there, let's get started"
        elif("/search" in msg):
                reply = "Sure!, here you go: "
                query =  msg
                query = "https://www.iiitd.ac.in:" + query.replace("/search","")
                for j in search(query, tld="co.in", num=1, stop=1, pause=1):
                    reply = reply+j
                return reply
        elif(msg == "/help"):
            reply = "have a look at our documentations"
        else:
            reply = "lemme have a look..."
    elif msg.lower() == "thanks":
        reply = "no problem"
    else:
        print("going for recog.")
        line = nltkk.execute(msg)
        try:
            print(line,"vfdvf")
            if type(line) is int:
                x = "data"+ str(line) +".txt"
                f = open(x, "r")
                line = f.read()
                f.close() 
            reply = line
        except:
            reply = "Unsupported"
            
    if(reply == None):
        reply = ""
    return reply
