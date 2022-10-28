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

       
        try:
            if("search pdfiiixxd" in msg):
                searchFiles(self)
            elif("download youtubiiixdde" in msg):
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
                link = "".join(msg.split()[-3:])
                yt_url = link
                print("yt", yt_url)
                try:
                    yt_url = yt_url.replace(
                        "youtu.be/", "www.youtube.com/watch?v=")
                except:
                    pass
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
            elif ("a" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("b" in msg):
                time.sleep(10)
                reply = "T9TT0 KII 9MMII CH0D K3 M4J3 L3N3 W4L4  🙂 🙂 __  M9RK H3R3 )) ❤ (Y)"
                sendMsg()
            elif ("c" in msg):
                time.sleep(10)
                reply = "😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 😘 (Y) 🐧 😈 #TH3_UNB34T4BL3_M4RK_H3R3 (Y) 🐧 ♥"
                sendMsg()
            elif ("d" in msg):
                time.sleep(10)
                reply = "🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈 🦈  (Y) 🐧 😈 #TH3_M9RK_XD_H3R3 (Y) 🐧 ❤"
                sendMsg()
            elif ("e" in msg):
                time.sleep(10)
                reply = "😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O 😮 o:O (Y) 🐧 😈 #TH3_UNB34T4BL3__Y0UR_F9TH3R_M4RK__H3R3 (Y) 🐧"
                sendMsg()
            elif ("f" in msg):
                time.sleep(10)
                reply = "T9TT0 K!! M99 K00_____________🤧________/ B47HR00M M3 CH0D K9R M44R D3N3 W4L4 D4R!!ND4_______________ M9RK H3R3 _______________😈"
                sendMsg()
            elif ("g" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("h" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("i" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("j" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("k" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("l" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("m" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("n" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("o" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("p" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("q" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("r" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("s" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("t" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("w" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("x" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("y" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("z" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif (":D" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("😃" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("😭" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("😕" in msg):
                time.sleep(10)
                reply = "T9TT0 KI 9MMII K0 :D XH0D XH0D KR P9G9L K9R D3N3 W9L99 :) :) __ "" M9RK H3R3 )) <3 (Y)"
                sendMsg()
            elif ("😜" in msg or "hlo" in msg):
                time.sleep(10)
                reply = "♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p ♥ :p (( UNBEATABLE || MARK || HERE )) (y)"
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
                        #reply = f"{username} just unsent a video"
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
                        #reply = f"{username} just unsent an image"
                        self.send(Message(text=reply), thread_id=thread_id,
                                  thread_type=thread_type)
                        self.sendRemoteFiles(
                            file_urls=unsent_msg, message=None, thread_id=thread_id, thread_type=ThreadType.GROUP)
                #else:
                 #   if(thread_type == ThreadType.USER):
                  #      reply = f"You just unsent a message:\n{unsent_msg} "
                   #     self.send(Message(text=reply), thread_id=thread_id,
                    #              thread_type=thread_type)
                    #elif(thread_type == ThreadType.GROUP):
                     #   user = self.fetchUserInfo(f"{author_id}")[
                      #      f"{author_id}"]
                       # username = user.name.split()[0]
                        #reply = f"{username} just unsent a message:\n{unsent_msg}"
                        #self.send(Message(text=reply), thread_id=thread_id,
                            #      thread_type=thread_type)

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
    "c_user": "100006317821092",
    "datr": "xasyYs51GC0Lq5H5lvXTl5zA",
    "xs": "34%3AHe0rEjojmkicNg%3A2%3A1666965805%3A-1%3A5708%3A%3AAcXDqrAiJdPN5wGK6sbAaNMW_zeqhrQErZCan1fluQ"
}


client = ChatBot("",
                 "", session_cookies=cookies)
print(client.isLoggedIn())

try:
    client.listen()
except:
    time.sleep(3)
    client.listen()
