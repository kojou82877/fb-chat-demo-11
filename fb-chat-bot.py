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

        def searchFiles(self):
            query = " ".join(msg.split()[2:])
            file_urls = []
            url = "https://filepursuit.p.rapidapi.com/"

            querystring = {"q": query, "filetype": msg.split()[1]}

            headers = {
                'x-rapidapi-host': "filepursuit.p.rapidapi.com",
                'x-rapidapi-key': "801ba934d6mshf6d2ea2be5a6a40p188cbejsn09635ee54c45"
            }

            response = requests.request(
                "GET", url, headers=headers, params=querystring)

            response = json.loads(response.text)
            file_contents = response["files_found"]
            try:
                for file in random.sample(file_contents, 10):
                    file_url = file["file_link"]
                    file_name = file["file_name"]
                    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                              thread_id=thread_id, thread_type=ThreadType.USER)
            except:
                for file in file_contents:
                    file_url = file["file_link"]
                    file_name = file["file_name"]
                    self.send(Message(text=f'{file_name}\n Link: {file_url}'),
                              thread_id=thread_id, thread_type=ThreadType.USER)

       
        try:
            if("search pdf" in msg):
                searchFiles(self)

            elif("search image" in msg):
                imageSearch(self, msg)

            elif("program to" in msg):
                programming_solution(self, msg)
            elif("translate" in msg):
                reply = translator(self, msg, msg.split()[-1])

                sendQuery()
            elif "weather of" in msg:
                indx = msg.index("weather of")
                query = msg[indx+11:]
                reply = weather(query)
                sendQuery()
            elif "corona of" in msg:
                corona_details(msg.split()[2])
            elif ("calculus" in msg):
                stepWiseCalculus(" ".join(msg.split(" ")[1:]))
            elif ("algebra" in msg):
                stepWiseAlgebra(" ".join(msg.split(" ")[1:]))
            elif ("query" in msg):
                stepWiseQueries(" ".join(msg.split(" ")[1:]))

            elif "find" in msg or "solve" in msg or "evaluate" in msg or "calculate" in msg or "value" in msg or "convert" in msg or "simplify" in msg or "generate" in msg:
                app_id = "Y98QH3-24PWX83VGA"
                client = wolframalpha.Client(app_id)
                query = msg.split()[1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                reply = f'Answer: {answer.replace("sqrt", "√")}'
                sendQuery()

            elif ("search user" in msg or "search friend" in msg):
                searchForUsers(self)

            elif("mute conversation" in msg):
                try:
                    self.muteThread(mute_time=-1, thread_id=author_id)
                    reply = "muted 🔕"
                    sendQuery()
                except:
                    pass
            elif ("busy" in msg):
                reply = "Nobody is busy. Only things are prioritized."
                sendMsg()
            elif ("akhil" in msg):
                reply = "Akhiil to riyan ka beta hai :)."
                sendMsg()
            elif ("ishita" in msg):
                reply = "Kammo and ishita are One heart and One soul <3."
                sendMsg()
            elif ("i love u" in msg):
                reply = "I love you more <3"
                sendMsg()
            elif ("really love me" in msg):
                reply = "yes i do <3"
                sendMsg()
            elif ("hi bot" in msg):
                reply = "hello i'm here :)"
                sendMsg()
            elif ("No" in msg):
                reply = "Yes!"
                sendMsg()
            elif ("who is atif" in msg):
                reply = "Oh Atif The God  Father of Haters kid."
                sendMsg()
            elif ("gand dede" in msg):
                reply = "land lele bhai :)."
                sendMsg()
            elif ("akku" in msg):
                reply = "love you akku (akhil) 😘❤️"
                sendMsg()
            elif ("i'm sad" in msg):
                reply = "Don't worry i am with you."
                sendMsg()
            elif ("i love you" in msg):
                reply = "I love you too <3"
                sendMsg()
            elif ("riyaan" in msg):
                reply = "Akhiil ka beta he riyaan "
                sendMsg()
            elif ("who is kammo" in msg):
                reply = "Kammo is my second love :)"
                sendMsg()
            elif("help" in msg):
                reply = "Sure! What should I do?"
                sendMsg()
            elif("rachit" in msg):
                reply = "wahi rachit jo ek number ka gandu hai??"
                sendMsg()
            elif("boyfriend" in msg):
                reply = "Kojou is my boyfriend"
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
                reply = "I am from India. Currently living in Kathmandu"
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
                        reply = f"You just unsent a video"
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
                        reply = f"You just unsent an image"
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

    def onColorChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        reply = "You changed the theme ✌️😎"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onEmojiChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        reply = "You changed the emoji 😎. Great!"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onImageChange(self, mid=None, author_id=None, new_color=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        reply = "This image looks nice. 💕🔥"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onNicknameChange(self, mid=None, author_id=None, new_nickname=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        reply = f"You just changed the nickname to {new_nickname} But why? 😁🤔😶"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onReactionRemoved(self, mid=None, author_id=None, thread_id=None, thread_type=ThreadType.USER, **kwargs):
        reply = "You just removed reaction from the message."
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onCallStarted(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
        reply = "You just started a call 📞🎥"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onCallEnded(self, mid=None, caller_id=None, is_video_call=None, thread_id=None, thread_type=None, ts=None, metadata=None, msg=None, ** kwargs):
        reply = "Bye 👋🙋‍♂️"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)

    def onUserJoinedCall(mid=None, joined_id=None, is_video_call=None,
                         thread_id=None, thread_type=None, **kwargs):
        reply = f"New user with user_id {joined_id} has joined a call"
        self.send(Message(text=reply), thread_id=thread_id,
                  thread_type=thread_type)


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
