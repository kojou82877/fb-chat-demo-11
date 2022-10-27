from fbchat import Client, log, _graphql
from fbchat.models import *
import json
import random
import wolframalpha
import requests
import time
import math
import sqlite3
from bs4 import BeautifulSoup
import os
import concurrent.futures
from difflib import SequenceMatcher, get_close_matches



class ChatBot(Client):

    def onMessage(self, mid=None, author_id=None, message_object=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        try:
            msg = str(message_object).split(",")[15][14:-1]

            if ("//video.xx.fbcdn" in msg):
                msg = msg

            else:
                msg = str(message_object).split(",")[19][20:-1]
        except:
            try:
                msg = (message_object.text).lower()
                print(msg)
            except:
                pass
        def sendMsg():
            if (author_id != self.uid):
                self.send(Message(text=reply), thread_id=thread_id,
                          thread_type=thread_type)

        def sendQuery():
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=thread_type)
        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                CREATE TABLE IF NOT EXISTS "{}" (
                    mid text PRIMARY KEY,
                    message text NOT NULL
                );

                """.format(str(author_id).replace('"', '""')))

                c.execute("""

                INSERT INTO "{}" VALUES (?, ?)

                """.format(str(author_id).replace('"', '""')), (str(mid), msg))
                conn.commit()
                conn.close()
            except:
                pass

        #def searchFiles(self):
         #   query = " ".join(msg.split()[2:])
          #  file_urls = []
           # url = "https://filepursuit.p.rapidapi.com/"

            #querystring = {"q": query, "filetype": msg.split()[1]}

            #headers = {
             #   'x-rapidapi-host': "filepursuit.p.rapidapi.com",
              #  'x-rapidapi-key': "801ba934d6mshf6d2ea2be5a6a40p188cbejsn09635ee54c45"
            #}

            #response = requests.request(
             #   "GET", url, headers=headers, params=querystring)

            #response = json.loads(response.text)
            #file_contents = response["files_found"]
            #try:
             #   for file in random.sample(file_contents, 10):
              #      file_url = file["file_link"]
               #     file_name = file["file_name"]
                #    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                 #             thread_id=thread_id, thread_type=ThreadType.USER)
            #except:
             #   for file in file_contents:
              #      file_url = file["file_link"]
               #     file_name = file["file_name"]
                #    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                 #             thread_id=thread_id, thread_type=ThreadType.USER)

       
        #try:
            #if("search pdfiiixxd" in msg):
             #   searchFiles(self)
            #elif("download youtubiiixdde" in msg):
             #   headers = {
              #      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
               # link = "".join(msg.split()[-3:])
                #yt_url = link
                #print("yt", yt_url)
                #try:
                 #   yt_url = yt_url.replace(
                  #      "youtu.be/", "www.youtube.com/watch?v=")
                #except:
                 #   pass
                #yt_url = yt_url.replace("youtube", "clipmega")
                #url = requests.get(yt_url, headers=headers)
                #soup = BeautifulSoup(url.text, "html.parser")
                #link = soup.select(".btn-group > a")
                #link = link[0]
                #link = str(link)
                #indx = link.find("href=")
                #indx_l = link.find("extension=mp4")
                #link = link[indx+6:indx_l+13].replace("amp;", "")
                #link = link.replace(" ", "%20")
                #final_link = link
                #print("final", final_link)
                #self.sendRemoteFiles(
                 #   file_urls=final_link, message=None, thread_id=thread_id, thread_type=thread_type)
            #elif("sarkojouch imakojouge" in msg):
             #   imageSearch(self, msg)

            #elif("prokojougram tkojouo" in msg):
             #   programming_solution(self, msg)
            #elif("trakojounslate" in msg):
             #   reply = translator(self, msg, msg.split()[-1])

                #sendQuery()
            elif "weakojouther okojouf" in msg:
                indx = msg.index("weathkojouer okojouf")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()
            elif "corokojouna okojouf" in msg:
                corona_details(msg.split()[2])
            elif ("calckojouulus" in msg):
                stepWiseCalculus(" ".join(msg.split(" ")[1:]))
            elif ("algekojoubra" in msg):
                stepWiseAlgebra(" ".join(msg.split(" ")[1:]))
            elif ("qkojouuery" in msg):
                stepWiseQueries(" ".join(msg.split(" ")[1:]))

            elif "fikojound" in msg:
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                query = msg.split()[1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                reply = f'Answer: {answer.replace("sqrt", "√")}'
                sendQuery()

            elif ("searkojouch ukojouser" in msg or "seakojourch frikojoukojouend" in msg):
                searchForUsers(self)

            elif("mkojouute convekojoursation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "xd 🔕"
                    sendQuery()
                except:
                    pass
            elif ("busy" in msg):
                reply = "Nobody is busy. Only things are prioritized."
                sendMsg()
            elif("help" in msg):
                reply = "Sure! What should I do?"
                sendMsg()
            elif("clever" in msg):
                reply = "Yes, i am clever. hope you will be clever soon."
                sendMsg()
            elif("crazy" in msg):
                reply = "Anything wrong about that."
                sendMsg()
            elif ("are funny" in msg):
                reply = "No. I am not. You are."
                sendMsg()
            elif ("marry me" in msg):
                reply = "Yes, if you are nice and kind girl. But if you are boy RIP."
                sendMsg()
            elif ("you from" in msg):
                reply = "I am from Nepal. Currently living in Kathmandu"
                sendMsg()
            elif ("you sure" in msg):
                reply = "Yes. I'm sure."
                sendMsg()
            elif ("great" in msg):
                reply = "Thanks!"
                sendMsg()
            elif ("no problem" in msg):
                reply = "Okay😊🙂"
                sendMsg()
            elif ("thank you" in msg):
                reply = "You're welcome😊🙂"
                sendMsg()
            elif ("thanks" in msg):
                reply = "You're welcome🙂"
                sendMsg()
            elif ("well done" in msg):
                reply = "Thanks🙂"
                sendMsg()
            elif ("wow" in msg):
                reply = "🙂😊"
                sendMsg()
            elif ("wow" in msg):
                reply = "🙂😊"
                sendMsg()
            elif ("bye" in msg):
                reply = "bye👋"
                sendMsg()
            elif ("good morning" in msg):
                reply = "Good Morning🌅🌺"
                sendMsg()
            elif ("goodnight" in msg):
                reply = "good night🌃🌙"
                sendMsg()
            elif ("good night" in msg or msg == "gn"):
                reply = "good night🌃🌙"
                sendMsg()
            elif ("hello" in msg):
                reply = "Hi"
                sendMsg()
            elif ("hello" in msg or "hlo" in msg):
                reply = "Hi"
                sendMsg()
            elif (msg == "hi"):
                reply = "Hello! How can I help you?"
                sendMsg()

        except Exception as e:
            print(e)

        self.markAsDelivered(author_id, thread_id)

    def onMessageUnsent(self, mid=None, author_id=None, thread_id=None, thread_type=None, ts=None, msg=None):

        if(author_id == self.uid):
            pass
        else:
            try:
                conn = sqlite3.connect("messages.db")
                c = conn.cursor()
                c.execute("""
                SELECT * FROM "{}" WHERE mid = "{}"
                """.format(str(author_id).replace('"', '""'), mid.replace('"', '""')))

                fetched_msg = c.fetchall()
                conn.commit()
                conn.close()
                unsent_msg = fetched_msg[0][1]

                if("//video.xx.fbcdn" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        reply = f"{username} just unsent a video"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                elif("//scontent.xx.fbc" in unsent_msg):

                    if(thread_type == ThreadType.USER):
                        
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.USER)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                else:
                    if(thread_type == ThreadType.USER):
                        reply = f"You just unsent a message:\n{unsent_msg} "
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                    elif(thread_type == ThreadType.GROUP):
                        user = self.fetchUserInfo(f"{author_id}")[
                            f"{author_id}"]
                        username = user.name.split()[0]
                        reply = f"{username} just unsent a message:\n{unsent_msg}"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)

            except:
                pass

    #def onColorChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You changed the theme ✌️😎"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onEmojiChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You changed the emoji 😎. Great!"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onImageChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "This image looks nice. 💕🔥"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onNicknameChange(self, mid=None, author_id=None, new_nickname=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = f"You just changed the nickname to {new_nickname} But why? 😁🤔😶"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onReactionRemoved(self, mid=None, author_id=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
     #   reply = "You just removed reaction from the message."
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onCallStarted(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
     #   reply = "You just started a call 📞🎥"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onCallEnded(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
     #   reply = "Bye 👋🙋‍♂️"
      #  self.send(Message(text=reply), thread_id=thread_id,
       #           thread_type=thread_type)

    #def onUserJoinedCall(mid=None, joined_id=None, is_video_call=None,
     #                    thread_id=None, thread_type=None, **kwargs):
      #  reply = f"New user with user_id {joined_id} has joined a call"
       # self.send(Message(text=reply), thread_id=thread_id,
        #          thread_type=thread_type)


cookies = {
    "sb": "xasyYmAoy1tRpMGYvLxgkHBF",
    "fr": "0NxayJuewRHQ30OX3.AWVJwIYNh0Tt8AJv6kSwDamhkoM.BiMrVd.Iu.AAA.0.0.BiMtVZ.AWXMVaiHrpQ",
    "c_user": "100077465853624",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "39%3AYKuia2tT7sRzng%3A2%3A1666800840%3A-1%3A4136%3A%3AAcVX2xzjnGcZqD_hPtmZH3uzvKbsGASsWXkgJoTX_g"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
