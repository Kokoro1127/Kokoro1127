import random
import time
import requests
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
from emotes import Dance_Floor
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata,  GetMessagesRequest, User ,Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
from highrise.__main__ import *
import asyncio, random
from emotes import Emotes
from emotes import Dance_Floor
import random
import time
from highrise import *
from highrise.webapi import *
from highrise.models_webapi import *
from highrise.models import *
from highrise import BaseBot, Position, User, AnchorPosition, GetMessagesRequest
import asyncio, random
from highrise.__main__ import *
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata
import re
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from typing import Any, Dict, Union
import random
import time
from highrise import BaseBot, Highrise, Position, AnchorPosition, Reaction
from highrise import __main__
from asyncio import run as arun
import asyncio
from random import choice
import json
from typing import List
from datetime import datetime, timedelta
from highrise.models import SessionMetadata

from highrise import BaseBot, __main__, CurrencyItem, Item, Position, AnchorPosition, SessionMetadata, User
from highrise.__main__ import BotDefinition
from asyncio import run as arun
from json import load, dump
import asyncio
import os
from highrise.models import SessionMetadata, User, Item, Position, CurrencyItem, Reaction
from highrise import BaseBot, Position
from highrise import __main__
from highrise.models import Item
from asyncio import run as arun
from highrise.models import AnchorPosition
import requests
from highrise import BaseBot, __main__
from highrise.models import (AnchorPosition, Item, Position, User,)
from highrise import BaseBot
from collections import UserDict
from highrise.models import SessionMetadata, User
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition
from highrise.models import Position
from highrise.models import SessionMetadata, User, CurrencyItem, Item, AnchorPosition, Reaction, ModerateRoomRequest, Position
import random
from highrise import *
from highrise.models import *
import asyncio
from asyncio import Task
from typing import Union
import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *

import asyncio
import contextlib
import random
from typing import Any, Dict, Union
from importlib.machinery import ModuleSpec
from click.decorators import pass_context
from highrise import BaseBot
from typing import Any, Dict, Union
from highrise import *
from highrise.models import *
from asyncio import Task
from highrise.__main__ import *
from highrise.models import (
    AnchorPosition,
    Item,
    Position,
    SessionMetadata,
    User,
)
from highrise.models import (
    CurrencyItem,
    GetMessagesRequest,
    Item,
    SessionMetadata,
)
import random
import requests
import os
import importlib
import asyncio
import contextlib
import logging
from highrise import BaseBot, AnchorPosition, Position, User, TaskGroup
moderators = ['_Toxic_Angel_','Mathaniel','DEMON_EJ_11','RainHaze','tomyHR']
mods = ['_Toxic_Angel_','Mathaniel','RainHaze']

class BotDefinition:


    def __init__(self, bot, room_id, api_token):
        self.bot = bot
        self.room_id = room_id
        self.api_token = api_token
        self.following_username = None

class Counter:
    bot_id = ""
    static_ctr = 0
    usernames = ['tomyHR']

class Bot(BaseBot):
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    continuous_emote_task = None
    cooldowns = {}  # Class-level variable to store cooldown timestamps
    emote_looping = False



    def __init__(self):
        super().__init__()
        self.load_membership()
        self.load_moderators()
        self.load_temporary_vips()
        self.following_username = None
        self.maze_players = {}
        self.user_points = {}  # Dictionary to store user points
        self.Emotes = Emotes
        self.should_stop = False
        self.announce_task = None
        #conversation id var
        self.convo_id_registry = []
        #dance floor position
        min_x = 10.5
        max_x = 16
        min_y = 0.25
        max_y = 0.25
        min_z = 19.5
        max_z = 25.5

        self.dance_floor_pos = [(min_x, max_x, min_y, max_y, min_z, max_z)]

        #dancer variable
        self.dancer = []

        #dance floor emotes var
        self.emotesdf = Dance_Floor
        #conversation id var
        self.convo_id_registry = []


    def load_temporary_vips(self):
        try:
            with open("temporary.json", "r") as file:
                self.temporary_vips = json.load(file)
        except FileNotFoundError:
            self.temporary_vips = {}

    def save_temporary_vips(self):
      with open("temporary.json", "w") as file:
          json.dump(self.temporary_vips, file)
    def load_moderators(self):
        try:
            with open("moderators.json", "r") as file:
                self.moderators = json.load(file)
        except FileNotFoundError:
            self.moderators = []

        # Add default moderators here
        default_moderators = ['ERROR_696','tomyHR']
        for mod in default_moderators:
            if mod.lower() not in self.moderators:
                self.moderators.append(mod.lower())

    def load_membership(self):
     try:
        with open("membership.json", "r") as file:
            self.membership = json.load(file)
     except FileNotFoundError:
        self.membership = []
    def save_membership(self):
     with open("membership.json", "w") as file:
        json.dump(self.membership, file)



    def save_moderators(self):

      with open("moderators.json", "w") as file:
            json.dump(self.moderators, file)

    async def dance_floor(self):

        while True:

            try:
                if self.dance_floor_pos and self.dancer:
                    ran = random.randint(1, 73)
                    emote_text, emote_time = await self.get_emote_df(ran)
                    emote_time -= 1

                    tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id)) for user_id in self.dancer]

                    await asyncio.wait(tasks)

                    await asyncio.sleep(emote_time)

                await asyncio.sleep(4)

            except Exception as e:
                print(f"{e}")
    async def get_emote_df(self, target) -> None:

        try:
            emote_info = self.emotesdf.get(target)
            return emote_info      
        except ValueError:
            pass
    async def announce(self, user_input: str, message: str):
      while not self.should_stop:  
          await asyncio.sleep(6)
          await self.highrise.chat(user_input)
          await asyncio.sleep(60)
          await self.highrise.send_emote('emote-hello')

          if message.lower().startswith("-announce "):
              parts = message.split()
              if len(parts) >= 3:
                  user_input = message[len("-announce "):]
                  await self.announce(user_input, message)

    def stop_announce(self):
      self.should_stop = True
      if self.announce_task is not None:
          self.announce_task.cancel()

    async def start_announce(self, user_input: str, message: str):
      if self.announce_task is not None:
          return
      self.announce_task = asyncio.create_task(self.announce(user_input, message))

    async def on_start(self, session_metadata: SessionMetadata) -> None:
      try:
         asyncio.create_task(self.dance_floor())
         Counter.bot_id = session_metadata.user_id
         print("bot comming ...")


         self.highrise.tg.create_task(self.highrise.walk_to(Position(x=11.5, y=0.0, z=6.5, facing='FrontRight')))
         self.load_temporary_vips()
         self.load_moderators()
         await asyncio.sleep(16)
         if Counter.bot_id not in self.dancer:
           self.dancer.append(Counter.bot_id)












      except Exception as e:
          print(f"An exception occured: {e}")  
    async def on_emote(self, user: User ,emote_id : str , receiver: User | None )-> None:
      print (f"{user.username} , {emote_id}")






    async def teleport_requester_to_user(self, target_username: str, requester_user: User):
      room_users = await self.highrise.get_room_users()
      target_user_position = None

      for user, position in room_users.content:
          if user.username.lower() == target_username.lower():
              target_user_position = position
              break

      if target_user_position is not None:
          requester_position = Position(target_user_position.x, target_user_position.y, target_user_position.z + 1, target_user_position.facing)
          requester_dict = {
              "id": requester_user.id,
              "position": requester_position
          }
          await self.highrise.teleport(requester_dict["id"], requester_dict["position"])
      else:
          print("Target user not found.")


    async def teleport_user_next_to(self, target_username: str, requester_user: User):
        room_users = await self.highrise.get_room_users()
        requester_position = None

        for user, position in room_users.content:
          if user.id == requester_user.id:
              requester_position = position
              break
        for user, position in room_users.content:
          if user.username.lower() == target_username.lower(): 
            z = requester_position.z 
            new_z = z + 1 

            user_dict = {
              "id": user.id,
              "position": Position(requester_position.x, requester_position.y, new_z, requester_position.facing)
            }
            await self.highrise.teleport(user_dict["id"], user_dict["position"])



    async def run(self, room_id, token):
        definitions = [BotDefinition(self, room_id, token)]
        await __main__.main(definitions) 



    async def follow_user(self, target_username: str):
      while self.following_username == target_username:
          # ابحث عن موقع المستخدم المستهدف في الغرفة
          response = await self.highrise.get_room_users()
          target_user_position = None
          for user_info in response.content:
              if user_info[0].username.lower() == target_username.lower():
                  target_user_position = user_info[1]
                  break

          if target_user_position:
              nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
              await self.highrise.walk_to(nearby_position)

              await asyncio.sleep(1)  # انتظر 5 ثواني مثلاً



    async def handle_order(self, user: User, message: str):

      food_prices = {
          "burger": 5,
          "sandwich": 3,
          "pizza": 10, 
          "hotdog": 5,
          "donuts": 4,
          "cake": 5,
          "coffee": 10,
          "hotchocolate": 20,
          "sushi": 5,
          "noodles": 4,
          "cookies": 5,
          "pancake": 4,
          "shrimp": 5,

      }
      items = message.split()[1:]
      items = [item for item in items if item != "and"]
      total_price = 0
      ordered_items = []
      for item in items:
          item_price = food_prices.get(item)
          if item_price:
              total_price += item_price
              ordered_items.append(item)

      if total_price > 0:
          await asyncio.sleep(5) 
          await self.highrise.chat(f"Preparing {item} .... ")

          await asyncio.sleep(5) 
          await self.highrise.walk_to(Position(x=16.5, y=7.75, z=16.5, facing='FrontLeft'))
          await asyncio.sleep(5) 
          await self.highrise.chat(f"wait 17 sec to finsh {item} ⏰")

          await self.highrise.walk_to(Position(x=17.5, y=7.75, z=16.5, facing='BackLeft'))
          await self.highrise.walk_to(Position(x=17.5, y=7.75, z=16.5, facing='BackLeft'))
          await asyncio.sleep(7)
          await self.highrise.walk_to(Position(x=16.5, y=7.75, z=16.5, facing='FrontLeft'))
          await asyncio.sleep(3)
          await self.highrise.chat(f"done {item}📿")
          await self.highrise.send_emote("emoji-thumbsup")

          await asyncio.sleep(7)
          await self.highrise.chat(f"next")


      else:
            await self.highrise.chat("not in menu please check menu")


    async def on_chat(self, user: User, message: str) -> None:

        print(f"{user.username}:{message}")



        user_input = None


        if message.startswith(("menu","!menu","Menu","list food","menu food","i want to order","how can i order")):
           food_menu = (
            f"\nMenu list :\n -burger \n -pizza \n -sandwich \n -hotdog \n -donuts \n -cake \n -coffee \n -hotchocolate \n -sushi \n -noodles \n -cookies \n -pancake \n -shrimp \n to order !order name any item you want in menu and bot will do it for you {user.username} Enjoy mel 😋")
           await self.highrise.chat(food_menu)

        if message.startswith(("i will take","i need","bot give me","!order","Order","order")):
          await self.handle_order(user, message)



        if message == "-cool46fh":
          shirt = ["shirt-n_room22019bratoppink"]
          pant = ["pants-n_room22019undiespink"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=3),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='nose-n_01_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=77),
                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='glasses-n_room32019smallshades', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018pillowfullpeaked', account_bound=False, active_palette=9),
                  Item(type='clothing', amount=1, id='eye-n_basic2018falselashes', account_bound=False, active_palette=10),
                  Item(type='clothing', amount=1, id='eyebrow-n_26', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")




        if message.lower().startswith("/need "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")

        if message.lower().startswith("!follow @"):
          if user.username in ["tomyHR", "_Toxic_Angel_", "Maithaei", "DEMON_EJ_11", "lovely123888", "Shadowslight"]:
            target_username = message.split("@")[1].strip()

            if target_username.lower() == self.following_username:
                await self.highrise.chat(f"I am already following {user.username}.")
            else:
                self.following_username = target_username
                await self.highrise.chat(f"follow {target_username}.")

                await self.follow_user(target_username)
        elif message.lower() == "!stop":
            self.following_username = None
            await self.highrise.chat("I have stopped following.")
        print (f"Received: {message} from {user.username}")

        if message.startswith("!heart ") and user.username in ["tomyHR", "_Toxic_Angel_", "Maithaei", "DEMON_EJ_11", "lovely123888", "Shadowslight"]: 
          try:

              parts = message.split()
              num_hearts = int(parts[-1])
              target_username = parts[1].strip('@').lower()

              if 1 <= num_hearts <= 100:
                  for _ in range(num_hearts):
                      target_user = None
                      response = await self.highrise.get_room_users()
                      for user_info in response.content:
                          if user_info[0].username.lower() == target_username:
                              target_user = user_info[0]
                              break

                      if target_user:
                          await self.highrise.react("heart", target_user.id)
                      else:
                          await self.highrise.chat(f"the user {target_username} Not available in the room.")
              else:
                  await self.highrise.chat("1  _ 100  only ")
          except ValueError:
              await self.highrise.chat("!heart @name number ")




        elif message.lower() == "!stop":
            self.following_username = None
            await self.highrise.chat("I have stopped following.")
        print (f"Received: {message} from {user.username}")

        if message.lower().startswith("-announce "):
          parts = message.split()
          self.should_stop = None
          if len(parts) >= 3:
              user_input =  message[len("-announce "):]
              await self.highrise.chat("Alright i will loop this message with intervals of 60 seconds.")
              await self.announce(user_input,message)
        if message.lower().startswith("-clear") :
           if user.username.lower() in self.moderators:
              await self.highrise.chat (f"Announcement message cleared")
              self.stop_announce()
              return

        if message.startswith("heart all"):
           if user.username.lower() in self.moderators:
             roomUsers = (await  self.highrise.get_room_users()).content
             for roomUser, _ in roomUsers:
                await self.highrise.react("heart", roomUsers.id)


        if message.startswith(("!loop ","Loop ","l ","L ","loop ")):
          parts = message.split()
          E = parts[1]
          E = int(E)
          emote_text, emote_time = await self.get_emote_E(E)
          emote_time -= 1
          user_id = user.id  
          if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
             await self.stop_continuous_emote(user.id)
             task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
             self.continuous_emote_tasks[user.id] = task
          else:
             task = asyncio.create_task(self.send_continuous_emote(emote_text,user_id,emote_time))
             self.continuous_emote_tasks[user.id] = task  



        elif message.lower().startswith(("stop","!stop","Stop","s","0")):
           if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
               await self.stop_continuous_emote(user.id)




        if message.lower().startswith("!buyvoice") and user.username in moderators:
            response = await self.highrise.buy_voice_time(payment="bot_wallet_only")
            print (response)

        if message.lower().startswith("!buyboost") and user.username in moderators:
            response = await self.highrise.buy_room_boost(payment="bot_wallet_only", amount=1)
            print (response)


        if message == "-fit2":
          shirt = ["shirt-n_starteritems2019femtshirtblack"]
          pant = ["skirt-n_room22019skirtwithsocksblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightpulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018longwavytopknot', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018femaleovalslant', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"good {xox}")

        if message == "-fit1":
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"good {xox}")






















#loop



#info user



#name item

        if message.lower().startswith("/getitem"):
          outfit_response = await self.highrise.get_my_outfit()
          fifth_item = outfit_response.outfit[4].id
          item_response = await self.webapi.get_item(item_id=fifth_item)
          print (item_response)

#heart all

        if message.startswith("-heart all"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
               await self.highrise.react("heart", roomUser.id)

#tip 5


        if message == ("/tip 2 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 3 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 4 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 5 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 6 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 7 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

        if message == ("/tip 8 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 9 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 10 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 20 5g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")

#tip 10g

        if message == ("/tip 2 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 3 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 4 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 5 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 6 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 7 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")

        if message == ("/tip 8 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 9 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 10 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


        if message == ("/tip 20 10g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_10")
              await self.highrise.chat(f"Tipped {roomUser.username} 10 gold.")


#tip 1

        if message == ("/tip 2 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:2]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 3 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:3]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 4 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:4]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 5 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:5]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 6 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:6]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 7 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:7]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

        if message == ("/tip 8 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:8]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")


        if message == ("/tip 9 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:9]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_5")
              await self.highrise.chat(f"Tipped {roomUser.username} 5 gold.")


        if message == ("/tip 10 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:10]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")     

        if message == ("/tip 20 1g") and user.username in moderators:
          roomUsers = (await self.highrise.get_room_users()).content
        # Shuffle the list to ensure randomness
          random.shuffle(roomUsers)
        # Select the first three users
          selected_users = roomUsers[:20]
          for roomUser, _ in selected_users:
              await self.highrise.tip_user(roomUser.id, "gold_bar_1")
              await self.highrise.chat(f"Tipped {roomUser.username} 1 gold.")

      #tip all


        if message.startswith("!tip ") and user.username in moderators:
          try:
              await self.highrise.chat(f"𝔫𝔬𝔴 𝔞𝔩𝔩 𝔤𝔢𝔱 𝔱𝔦𝔭 𝔣𝔯𝔬𝔪 @{user.username}")
              tip_amount = int(message.split(" ")[1])
          except IndexError:
              await self.highrise.chat("plz add how much you want to tip all")
              return
          except ValueError:
              await self.highrise.chat("CAN YOU WRITE THE RIGHT COMMAND !tip amount")
              return
          if user.username in['_Toxic_Angel_','Maithaei','DEMON_EJ_11','lovely123888','Shadowslight','tomyHR']:
              response = await self.highrise.get_room_users()
              num_users = len(response.content)
              total_gold = tip_amount * num_users

              bot_wallet = await self.highrise.get_wallet()
              bot_amount = bot_wallet.content[0].amount

              if bot_amount >= total_gold:
                  for content in response.content:
                      user_id = content[0].id
                      await self.highrise.tip_user(user_id, f"gold_bar_{tip_amount}")
              else:
                  await self.highrise.chat("send gold to send tips")

#mod commands


        if message.startswith("!kick"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !kick @username")
                  return

              mention = parts[1]
              username_to_kick = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_kick.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_kick.lower())
                  user_id_to_kick = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_kick, "kick")
                  await self.highrise.chat( f"Kicked {mention}.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")










        elif message.startswith("!mute"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !mute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",3600)  # Mute for 1 hour
                  await self.highrise.chat(f"Muted {mention} for 1 hour.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!unmute"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !mute @username")
                  return

              mention = parts[1]
              username_to_mute = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_mute.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_mute.lower())
                  user_id_to_mute = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_mute, "mute",1)  # Mute for 1 hour
                  await self.highrise.chat(f"{mention} Unmuted.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.startswith("!ban"):
          if user.username.lower() in self.moderators:
              parts = message.split()
              if len(parts) < 2:
                  await self.highrise.chat(user.id, "Usage: !ban @username")
                  return

              mention = parts[1]
              username_to_ban = mention.lstrip('@')  # Remove the '@' symbol from the mention
              response = await self.highrise.get_room_users()
              users = [content[0] for content in response.content]  # Extract the User objects
              user_ids = [user.id for user in users]  # Extract the user IDs

              if username_to_ban.lower() in [user.username.lower() for user in users]:
                  user_index = [user.username.lower() for user in users].index(username_to_ban.lower())
                  user_id_to_ban = user_ids[user_index]
                  await self.highrise.moderate_room(user_id_to_ban, "ban", 3600)  # Ban for 1 hour
                  await self.highrise.chat(f"Banned {mention} for 1 hour.")
              else:
                  await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
          else:
              await self.highrise.send_whisper(user.id, "You can't use this command.")




        if message.startswith("!time"):
          parts = message.split()
          if len(parts) == 2:
              target_mention = parts[1]

              # Remove the "@" symbol if present
              target_user = target_mention.lstrip('@')

              # Check if the target user has temporary VIP status
              remaining_time = self.remaining_time(target_user.lower())
              await self.highrise.send_whisper(user.id, f"Remaining time for {target_mention}'s temporary VIP status: {remaining_time}")
          else:
              await self.highrise.send_whisper(user.id, "Usage: !time @username")

#reaction

        if message.startswith(("i love you bot","بوت بحبك","بوت","بوت كيوت","البوت جامد","البوت جميل")):
            await self.highrise.react("heart", user.id)



        if message.lower().startswith("/getoutfit"):
            response = await self.highrise.get_my_outfit()
            for item in response.outfit:
                await self.highrise.chat(item.id)



#MASSGES


        if message.startswith(("!help","help","Help","!commands","commands")):
                help_message = (
                    "Available Commands:\ncommands you can use:\nsayso @username\nfight @username\nuwu @username\n Example: fight @tomy_x\nloop number 1 to 93\n!play rock or paper or scissors\nwrite any number start from 2 to no end\nf0 and f1 and f2 for teleports you in the room\nhatepercentage\njoke\nlovepercentage\ndeathyear\nRizz\ngo to the dance floor to emote with bot\n\nif you mod say !modcommands"


                    # ... (other commands)
                )

                # Chunk the message to avoid exceeding message length limits
                chunk_size = 250
                for i in range(0, len(help_message), chunk_size):
                    chunk = help_message[i : i + chunk_size]
                    await self.highrise.send_whisper(user.id, chunk)














      #TELEPORS

        if message.startswith(('!f0','F0','f0','!F0')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=8.5, y=0.25, z=1.5, facing='FrontRight'))

        if message.startswith(('!f1','f1','F1','!F1')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=8.5, y=5.75, z=1.5, facing='FrontRight'))

        if message.startswith(('!f3','F3','f3','!F3')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=9.5, y=14.0, z=1.5, facing='BackLeft'))

        if message.startswith(('!f2','F2','f2','!F2')):
           parts = message.split()
           if len(parts) == 1:
              await self.highrise.teleport(f"{user.id}", Position(x=11.5, y=10.75, z=1.5, facing='FrontRight'))

        if message.startswith("!vip"):
           if user.username.lower() in self.moderators:
              split = message.split()
              if len(split) == 2:
                  name = split[1].lower()
                  response = await self.highrise.get_room_users()
                  users = [content[0] for content in response.content]
                  try:
                      for u in users:
                          u_give = str("@") + str((u.username).lower())
                          if str((u_give).lower()).strip() == str(name).strip():
                              await self.highrise.teleport(u.id,Position(x=13.5, y=16.0, z=4.5, facing='FrontLeft')) 
                              break
                  except:
                      pass
              else:
                  await self.highrise.teleport(user.id,Position(x=13.5, y=16.0, z=4.5, facing='FrontLeft'))


        if message.lower().startswith(("!play","!rps","-rps","rps","play","-play","Play")):
          choices = ['rock', 'paper', 'scissors']
          client_chosen = random.choice(choices)
          option = message[5:].strip().lower()

          text_to_emoji = {"rock": "✊", "paper": "✋", "scissors": "✌️"}

          if option not in choices:
              response = f"Invalid command usage:\nExample: !rps <{client_chosen}>\nAvailable Options:\n{', '.join(choices)}"
              await self.highrise.send_whisper(user.id, response)
              return
          elif option == client_chosen:
              response = "Nobody has won, it's a tie. 🤝"
          elif (option == "rock" and client_chosen == "scissors") or (option == "paper" and client_chosen == "rock") or (option == "scissors" and client_chosen == "paper"):
              response = f"\nCongratulations, you won! 🎉\nYou: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"
          else:
              response = f"\nYou lost. 😢\nYou: {text_to_emoji[option]}\nBot: {text_to_emoji[client_chosen]}"

          await self.highrise.chat(response)

        if message.startswith("!down"):
           if user.username.lower() in self.moderators:
              split = message.split()
              if len(split) == 2:
                  name = split[1].lower()
                  response = await self.highrise.get_room_users()
                  users = [content[0] for content in response.content]
                  try:
                      for u in users:
                          u_give = str("@") + str((u.username).lower())
                          if str((u_give).lower()).strip() == str(name).strip():
                              await self.highrise.teleport(u.id,Position(x=1.5, y=0.0, z=0.5, facing='FrontRight')) 
                              break
                  except:
                      pass
              else:
                  await self.highrise.teleport(user.id,Position(x=1.5, y=0.0, z=0.5, facing='FrontRight'))

        #NAME ITEM

        if message.lower().startswith("/item "):
            parts = message.split(" ")
            if len(parts) < 2:
                await self.highrise.chat("Invalid command")
                return
            item_name = ""
            for part in parts[1:]:
                item_name += part + " "
            item_name = item_name[:-1]
            print (item_name)
            try:
                response = await self.webapi.get_items(item_name=item_name)
                print (response)
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")

      #WALLET

        if  message.startswith("!wallet"):
            if user.username in moderators :

                  wallet = (await self.highrise.get_wallet()).content
                  await self.highrise.send_whisper(user.id, f"bot have {wallet[0].amount} {wallet[0].type}")

            else: 
                await  self.highrise.send_whisper(user.id, f"your not mod")


      #ملابس

        if message == "!fit 1"  and user.username in moderators:
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullpeaked', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightbluntbangs', account_bound=False, active_palette=28),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straighthighpony', account_bound=False, active_palette=28),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2019flatsblack', account_bound=False, active_palette=0),



                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"تم {xox}")

        if message == "!fit 2" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterwhite"]
          pant = ["pants-n_room12019rippedpantsblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018mediumcurlymarilyn', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2018marilyncurls', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-f_blush01', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019hightopsblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-n_basic2018toothyfullpeaked', account_bound=False, active_palette=24),
                  Item(type='clothing', amount=1, id='eye-n_basic2018pinkshadow2', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])


          await self.highrise.chat(f"{xox}")

        if message == "!fit20" and user.username in moderators:
          shirt = ["shirt-n_room32019jerseywhite"]
          pant = ["pants-n_room22019longcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew16', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_03_b', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_malenew16', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairupper06', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='face_hair-n_newbasicfacehairlower16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamondsleepy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")

        if message == "!fit 3" and user.username in moderators:
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),

          ]) 
          await self.highrise.chat(f"good {xox}")


        if message.lower().startswith("/getinventory"):
            inventory = await self.highrise.get_inventory()
            print (inventory)


        if message.lower().startswith("/buy "):
            parts = message.split(" ")
            if len(parts) != 2:
                return "Invalid command"
            item_id = parts[1]
            try:
                response = await self.buy_item(item_id)
                return f"Item bought: {response}"
            except Exception as e:
                return f"Error: {e}"

# Example usage
            highrise_instance = Highrise()
            result = await highrise_instance.chat("/buy shirt-n_starteritems2019tankwhite")
            print(result)



        if message.lower().startswith(
        "delayed_message") and user.username in self.allowed_usernames:
                 await self.delayed_message_command(Message)

        elif message.lower(
    ) == "stop_delayed_message" and user.username in self.allowed_usernames:
                 await self.stop_delayed_messages()












        elif message.startswith("/come")and user.username in self.allowed_usernames:
                response = await self.highrise.get_room_users()
                your_pos = None
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            your_pos = content[1]
                            break
                if not your_pos:
                    await self.highrise.send_whisper(user.id, "Invalid coordinates!")
                    return
                await self.highrise.chat(f"@{user.username} I'm coming ..")
                await self.highrise.walk_to(your_pos)

        elif message.startswith("❤"):
            await self.highrise.react("heart", user.id)



        elif message.lower().startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"يوجد {len(room_users)} مستخدم في الغرفه")

        elif message.lower().startswith("outfit"):  
            print(await self.highrise.get_user_outfit(user.id))











        if "Rizz" in message:
            pickuplines = random.choice(["Do you believe in love at first sight, or should I walk by again?","Is your name Google? Because you have everything I've been searching for.","Are you a magician? Whenever I look at you, everyone else disappears.","Do you have a map? I keep getting lost in your eyes.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Excuse me, but I think you dropped something: my jaw.","Do you have a Band-Aid? Because I just scraped my knee falling for you.","Is your dad a boxer? Because you're a knockout!","Do you have a map? I keep getting lost in your eyes.","Is your name Google? Because you've got everything I've been searching for.","Do you have a name, or can I call you mine?","Are you a magician? Whenever I look at you, everyone else disappears.","Is your name Wi-Fi? Because I'm feeling a connection.","Do you have a sunburn, or are you always this hot?","Excuse me, but I think you dropped something: my jaw.","Is your dad a boxer? Because you're a knockout!","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Is your name Google? Because you've got everything I've been searching for.","Do you have a map? Because I keep getting lost in your eyes.","Are you a magician? Every time I look at you, everyone else disappears.","Do you believe in love at first sight, or should I walk by again?","Excuse me, but I think you dropped something: my jaw.","Is your name Wi-Fi? Because I'm feeling a connection.","If you were a vegetable, you'd be a cute-cumber.","Can I follow you home? Cause my parents always told me to follow my dreams.","Is your dad a boxer? Because you're a knockout!","Do you have a name, or can I call you mine?", "I hope you know CPR, because you just took my breath away!","So, aside from taking my breath away, what do you do for a living?" , " I ought to complain to Spotify for you not being named this week’s hottest single." , "Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.","Is your name Google? Because you've got everything I've been searching for.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you believe in love at first sight, or should I walk by again?","If you were a vegetable, you'd be a cute-cumber.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because every time I look at you, everyone else disappears.","Excuse me, but I think you dropped something: my jaw.","If you were a triangle, you'd be acute one.","Can I take you out for coffee, or do you prefer to brew it yourself?","Are you made of copper and tellurium? Because you're Cu-Te.","Are you a camera? Because every time I look at you, I smile.","Do you have a name, or can I call you mine?","Do you have a map? Because I keep getting lost in your eyes.","I must be a snowflake because I've fallen for you.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a Wi-Fi signal? Because I'm feeling a connection.","Do you believe in fate? Because I think we were meant to meet.","Are you a time traveler? Because I can see you in my future.","Do you have a name, or can I call you mine?","Can I borrow a kiss? I promise I'll give it back.","I must be a snowflake because I've fallen for you.","If you were a vegetable, you'd be a cute-cumber.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","If you hate me don't read this...Ok done it means you love me and I love you too congratulations we are in relationship...","i may not be a dentist but...I'll surely take care of that smile of yours","I don't have many pick up lines because I'm not trynna pick you up but pin you down","i love people with humor but i love hu-mor (humor rizz)","Are you a piano? Because I wanna use my fingers to play with you until you make beautiful noise!!!!!!!","Texting isn't enough I need you sitting on My lap facing me","Are you other peoples opinion? Cause I can't stop thinking about you (Social anxiety rizz)","Are u lamp of Aladin bcoz i wanna rub u down there and get all my wishes complete","Im glad you dad didn't pull out you're kinda Cool","The word of the day is 'LEGS' So why don't you come over and we can spread the word","I just wish I had more money instead of this massive cock.","Do yk the difference between history and you? History is the past & you are my future (History Rizz)","Are u the clock at school? Because I be lookin at u all day. (School clock rizz)","Are you a painting? Because i'd like to pin you against my wall (artist rizz)","Are you a box of chocolates? Cause I want to take your top off and eat you all night.","Math is incorrect they keep talking about x and y instead of u and i (algebraic rizz)","Why does everything have to be a relationship, We can't kiss and be friends?","In honor of pride month maz How about you let me She/Them T!ddies","I just say 'night' because if it was goodnight you'd be in my bed","You look kinda ill, you must be suffering from a lack of 'Vitamin ME'","Did you know that sleeping next to the person you like helps you fall asleep faster, reduces depression and makes you live longer so why aren't you here every night?"])
            await self.highrise.chat(f": {user.username} - {pickuplines}")

        if "Joke" in message or "joke" in message:
            joke = random.choice(["Yo mama's so fat, when she goes camping, the bears hide their food.", "Your mama's so fat she falls both sides of the bed" , "I wont tell ya lol", "Your mama's so stupid she studied for COVID test","Your mama so ugly when she goes to the dentist they make her lay face down","Your mama's so stupid she used a ruler to see how long she slept","Your mama's so fat her belt size is the size of the equator","Your mama's so ugly when she falls of the car, the driver gets arrested for littering" , "I told my wife she was drawing her eyebrows too high. She looked surprised.","Why don't scientists trust atoms? Because they make up everything.","What do you call fake spaghetti? An impasta.","Why don't skeletons fight each other? They don't have the guts.","I used to play piano by ear, but now I use my hands.","I'm on a whiskey diet. I've lost three days already.","What do you call a bear with no teeth? A gummy bear.","I told my wife she was drawing her eyebrows too low. She looked surprised.","The early bird might get the worm, but the second mouse gets the cheese.","Parallel lines have so much in common. It's a shame they'll never meet.","Why don't seagulls fly over the bay? Because then they'd be bagels.","How do you organize a space party? You planet.","Did you hear about the kidnapping at the playground? They woke up.","My boss told me to have a good day, so I went home.","Joke? Your whole life","i just found out if two girls are close, their period dates can change to be at the same time, tf kinda bluetooth is that","Remember if there's ever a person you like and are talking to, you should just cut off contact and block them because it's never gonna work","Nah cuz why tf do girls make code names for boys. Like who tf is 'Pineapple'"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "نكت" in message or "ضحكني" in message:
            joke = random.choice(["بنت في فوق عينها شامة شافها محشش وقالها هي عين أو غين", "واحد قام يساوي شاي لربع قام لاقى السكر خالص، فاضطر يعمل الشاي بدون سكر وقدمه لهم، وقال فيه كاسة بدون سكر اللي بتطلعله العشاء عليه الليلة، فكلهم شربوا الشاي وما حدا تكلم أبدًا." , "في وحدة كاتبة: سأوسيطرو على العالمي يومن مينا الأيامي”، انتِ سيطري على الكيبورد وبعدين منتفاهم.","م تسأل ولدها تعرف نيوتن؟، قال الولد: لا ما أعرفه، قالت له: لو تنتبه لدروسك كان عرفته!!، قال الولد: طيب أنتِ تعرفين خلود؟، قالت له: لا من هي؟، قال لها : لو تنتبهين لزوجك كان عرفتيها!!، المهم الولد حاليًا أسبوع عند أخواله وأسبوع عند عمامه.","محشش ومرتو المحششة قاعدين، قالت المرأة: نفسي أعرف ليش الناس بتحكي عنا نكت؟، قال لها: لأن رأسنا مثل هذه الطاولة، فدق على الطاولة دقتين، قالت زوجته: مين؟، قال لها: اقعدي أنا بفتح الباب.","بعض الشباب يرجع من لعب الكرة ويصف لعبه والمغامرات اللي واجهته، وآخر شيء لما ترى ركضه في الملعب بتقول فيلم وثائقي عن حياة النعامة.","واحد تخانق مع زوجته قال لها: ما رح أشبهك بالحمار أخاف يزعل!، قالت له: كل شيء ولا زعلك عاد، يقولون إبليس دمعت عيونه وصفق لها." , "مرة واحد سأل رفيقو شو يعمل مشان يقدر ينام، نصحه رفيقه أنه يعد للـ 100 وبكون غفا، فالزلمة قام يعد لما وصل للرقم 93 حس حاله رح يغفا، راح غسل وجهه وكمل عد.","هو ما يقدر ينام بدون ما يسمع صوتها، وهي لا تقدر تنام بدون ما يحكي لها، وأنا ما أقدر أنام والباب مفتوح، فكل واحد حسب رزقه.","الأب: تحبوني ولا تحبون أمكم أكثر؟، الأولاد: نحبكم كلكم..، الأب: طيب لو أنا رحت للمدينة وأمكم راحت مكة، أين تروحوا؟، الأولاد: نروح مكة، الأب: يعني تحبوا أمكم أكثر، الأولاد: لا.. بس نحب مكة، الأب: طيب إذا أنا رحت مكة أما أمكم راحت للمدينة، فين تروحوا؟، الأولاد: نروح المدينة، الأب: ليييش، الأولاد: لأنه نحن خلاص رحنا مكة….. تربية أمهم.","لو أحد تفلسف عليك وقال لك لازم دائمًا تتوقع في الدنيا الذي مش متوقعه، أعطيه كف ع قفاه بسرعة وقل له بذمتك توقعته!.","كيف بتصنع بابا غنوج: أولاً بتجيب أبوك، ثانيًا بتغنجو، وشوي شوي بيصير البابا غنوج","أمي بس تبهدل حدا من أخواتي مستحيل تبهدله لوحده لازم تتطرق للـ select all","أمّي لما تناديني بتنادي كل أخواتي وأنا قاعدة بتطلع فيها وبالآخر بتسلخني بالريموت وبتقولي ليش ما بتردي، طيب شو أعمل إذا اسمي ما اجا بالتشكيلة.","واحد قال لصاحبه عيب زوجتك تضربك بالشبشب واحنا قاعدين، قال له بس بزمتك اجت فيني شي مرة","مذيعة تسأل واحد مسطول أحمد زويل أخذ جائزة نوبل بشو، قالها في علبة قطيفة حمراء.","مرة واحدة اسمها سميرة عمارة قفزت فوق أبوها انتحرت.","مرّة واحد كان يشاهد مقطع ساخن قام .","مرة واحدة سايقة على الجي بي إس قالها انحرفي قليلًا قامت شالت الطرحة.","محشش غمز زوجته وقال لها اطلبي من العيال أن يناموا، صرخت الزوجة اللي ينام سيأخذ 100 ريال، قام نام زوجها أول واحد.","شرطي قبض على محشش قاله وين ساكن؟، قاله المحشش مع أخوي، قاله الشرطي وأخوك وين ساكن؟، قال له معي، قال الشرطي انت وأخوك وين ساكنين؟، قال المحشش مع بعض.","واحد سأل خطيبته في أحد مسك يدك؟، سكتت قال لها زعلتي، قالت له لا بس أعدهم.","وَاحد خبطته سيارة أخذ تعويض 70000، قام وقف أمام القطار وقال له خش عليا يا أبو الملايين."])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "اهلا بوت" in message or "hi bot" in message:
            joke = random.choice(["اهلا", "اهلا وسهلا" , "كيفك","القمر بيسلم"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "محتاج مساعده" in message or "بوت محتاج مساعده" in message:
            joke = random.choice(["كلم المشرفين هيسعدوك", "لو  محتاج اي مساعده كلم المشرفين او صاحب الروم"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "بوت ابعت جولد" in message or "ممكن جولد" in message:
            joke = random.choice(["اعع مش بكلم فقراء", "امم لازم تتعب عشان تجيب جولد مش تشحت" , "هوا فيه كدا بجد","لازم تتعب","اتعب عشان توصل للي عوزه"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "قمر" in message or "انت عسل" in message:
            joke = random.choice(["اوه انت الي عسل", "انت احلي يا قمر" , "اتكسفتتت","حقيقه ","ثانكس"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "تحبني" in message or "بتحبني" in message :
            joke = random.choice(["اوه طبعاا" , "لاع يععع","طبعا يا حياتي ","امم اعتقد شويه"])
            await self.highrise.chat(f": {user.username} - {joke}")

        if "انا بكرهك" in message or "بكرهك" in message or "كل تبن" in message:
            joke = random.choice(["بردك بجبك", "في ستين دهيه" , "انت فاكر نفسك مين","بابا فوق لي نفسك","شوف نفسك"])
            await self.highrise.chat(f": {user.username} - {joke}")




        if message.lower().lstrip().startswith(("!rules", "-rules", "-القواعد", "!القواعد", "اقواعد")):
           await self.highrise.chat(f"\n\n        RULES\n ____________________________\n 1. NO UNDERAGE \n 2. No advertising\n 3. No hate speech \n 4. No begging (those trash will be immediately banned 🚫) \n 5. No spamming\n ____________________________\n")
           await self.highrise.chat(f"\n\n        RULES\n ____________________________\n1. NO SER MENOR DE EDAD N 2. Sin publicidadn 3. No a la incitación al odio n 4. No mendigar (esa basura será prohibida 🚫 inmediatamente) n 5. Sin spam\n ____________________________\n")

        if message.lower().lstrip().startswith(("-emotefriend","!listemotefriend","!emotefriend","listemotefriend")):
           await self.highrise.send_whisper(user.id,"fight @name\nhug@name\nflirt@name\nstars @name\nzombie @name\n gravity @name\nuwu @name\nzero @name\n fashion @name\n icecream @name\n punk @name\nwrong @name\nsayso @name\ncutey @name\npose1 @name\npose3 @name\npose5 @name\npose7 @name\npose8 @name")
           await self.highrise.send_whisper(user.id,"dance @name\nshuffle @name\nviralgroove @name\n weird @name\n russian @name\n curtsy @nams\n snowball @name\n sweating @name\n snowangel @name\n cute @name\n worm @namen\n lambi @name\n sing @name\n frog @name\n ball @name\n maniac @name\n float @name")





        if message.lower().lstrip().startswith(("fight", "hug", "flirt", "stars", "gravity", "uwu", "zero","fashion", "icecream", "punk", "wrong", "sayso", "zombie", "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance", "shuffle", "viralgroove", "weird", "russian", "curtsy", "snowball", "sweating", "snowangel", "cute", "worm", "lambi", "sing", "frog", "energyball", "maniac", "teleport", "float", "telekinesis", "enthused", "confused", "charging", "shopping", "bow", "savage", "kpop", "model", "dontstartnow", "pennydance", "flex", "gagging", "greedy", "cursing", "kiss", "wing", "bashfull", "anime", "airguitar", "revelation", "penguin", "creepycute", "creepy", "sleigh", "hyped", "jingle", "nervous", "gottago", "timejump", "repose", "kawaii", "scritchy", "skating", "touch" )):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return

                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return


                if message.lower().lstrip().startswith("fight"):
                        await self.highrise.chat(f"\n🥷 @{user.username} And @{args[0][1:]} are in fight 🤬⚔️🔥")
                        await self.highrise.send_emote("emote-swordfight", user.id)
                        await self.highrise.send_emote("emote-swordfight", user_id)

                elif message.lower().lstrip().startswith("hug"):
                        await self.highrise.chat(f"\n🫂 @{user.username} And @{args[0][1:]} in love ❤️")
                        await self.highrise.send_emote("emote-hug", user.id)
                        await self.highrise.send_emote("emote-hug", user_id)

                elif message.lower().lstrip().startswith("flirt"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} so cool 🤭🫣❤️")
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                elif message.lower().lstrip().startswith("stars"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)


                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} fly in the moon😰😧👨🏻‍🚀")
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("gravity"):
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)

                elif message.lower().lstrip().startswith("uwu"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} shyyy🤭🫣❤️")
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                elif message.lower().lstrip().startswith("fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                elif message.lower().lstrip().startswith("icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                elif message.lower().lstrip().startswith("punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                elif message.lower().lstrip().startswith("wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                elif message.lower().lstrip().startswith("sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                elif message.lower().lstrip().startswith("zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                elif message.lower().lstrip().startswith("cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                elif message.lower().lstrip().startswith("pose5"):
                        await self.highrise.send_emote("emote-pose5", user.id)
                        await self.highrise.send_emote("emote-pose5", user_id)

                elif message.lower().lstrip().startswith("pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                elif message.lower().lstrip().startswith("pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                elif message.lower().lstrip().startswith("pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                elif message.lower().lstrip().startswith("pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                elif message.lower().lstrip().startswith("dance"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                elif message.lower().lstrip().startswith("shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                elif message.lower().lstrip().startswith("weird"):
                        await self.highrise.send_emote("emote-weird", user.id)
                        await self.highrise.send_emote("emote-weird", user_id)

                elif message.lower().lstrip().startswith("viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)

                elif message.lower().lstrip().startswith("cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                elif message.lower().lstrip().startswith("frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                elif message.lower().lstrip().startswith("lambi"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                elif message.lower().lstrip().startswith("sing"):
                        await self.highrise.send_emote("idle-singing", user.id)
                        await self.highrise.send_emote("idle-singing", user_id)

                elif message.lower().lstrip().startswith("worm"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                elif message.lower().lstrip().startswith("bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)

                elif message.lower().lstrip().startswith("energyball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                elif message.lower().lstrip().startswith("maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                elif message.lower().lstrip().startswith("teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                elif message.lower().lstrip().startswith("float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                elif message.lower().lstrip().startswith("telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                elif message.lower().lstrip().startswith("enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                elif message.lower().lstrip().startswith("confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                elif message.lower().lstrip().startswith("shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                elif message.lower().lstrip().startswith("charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                elif message.lower().lstrip().startswith("snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                elif message.lower().lstrip().startswith("sweating"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                elif message.lower().lstrip().startswith("snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                elif message.lower().lstrip().startswith("curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                elif message.lower().lstrip().startswith("russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                elif message.lower().lstrip().startswith("pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                elif message.lower().lstrip().startswith("dont"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                elif message.lower().lstrip().startswith("kpop"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                elif message.lower().lstrip().startswith("model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)

                elif message.lower().lstrip().startswith("savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)

                elif message.lower().lstrip().startswith("flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                elif message.lower().lstrip().startswith("gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)

                elif message.lower().lstrip().startswith("greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                elif message.lower().lstrip().startswith("cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)

                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("eote-kiss", user_id)
                elif message.lower().lstrip().startswith("anime"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user.id)
                elif message.lower().lstrip().startswith("airguitar"):
                        await self.highrise.send_emote("idle-guitar", user.id)
                        await self.highrise.send_emote("idle-guitar", user_id)
                elif message.lower().lstrip().startswith("revelations"):
                        await self.highrise.send_emote("emote-headblowup", user.id)
                        await self.highrise.send_emote("emote-headblowup", user_id)
                elif message.lower().lstrip().startswith("creepy"):
                        await self.highrise.send_emote("dance-creepypuppet", user.id)
                        await self.highrise.send_emote("dance-creepypuppet", user_id)
                elif message.lower().lstrip().startswith("creepycute"):
                        await self.highrise.send_emote("emote-creepycute", user.id)
                        await self.highrise.send_emote("emote-creepycute", user.id)
                elif message.lower().lstrip().startswith("penguin"):
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user.id)
                elif message.lower().lstrip().startswith("sleigh"):
                        await self.highrise.send_emote("emote-sleigh", user.id)
                        await self.highrise.send_emote("emote-sleigh", user.id)
                elif message.lower().lstrip().startswith("hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user.id)
                elif message.lower().lstrip().startswith("jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                elif message.lower().lstrip().startswith("nervous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user.id)
                elif message.lower().lstrip().startswith("toilet"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user.id)
                elif message.lower().lstrip().startswith("timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("dance-skating", user.id)
                        await self.highrise.send_emote("dance-skating", user.id)
                elif message.lower().lstrip().startswith("repose"):
                        await self.highrise.send_emote("sit-relaxed", user.id)
                        await self.highrise.send_emote("sit-relaxed", user.id)
                elif message.lower().lstrip().startswith("kawaii"):
                        await self.highrise.send_emote("dance-kawai", user.id)
                        await self.highrise.send_emote("dance-kawai", user.id)
                elif message.lower().lstrip().startswith("scritchy"):
                        await self.highrise.send_emote("idle-wild", user.id)
                        await self.highrise.send_emote("idle-wild", user.id)
                elif message.lower().lstrip().startswith("skating"):
                        await self.highrise.send_emote("emote-iceskating", user.id)
                        await self.highrise.send_emote("emote-iceskating", user.id)

                elif message.lower().lstrip().startswith("touch"):
                        await self.highrise.send_emote("dance-touch", user.id)
                        await self.highrise.send_emote("dance-touch", user.id)


        if message.startswith("0"):
          await self.highrise.send_emote("emote-float", user.id)
        if message.startswith("1"):
          await self.highrise.send_emote("dance-macarena", user.id)
        if message.startswith("2"):
          await self.highrise.send_emote("dance-tiktok2", user.id)   
        if message.startswith("3"):
          await self.highrise.send_emote("emote-pose1", user.id)
        if message.startswith("4"):
          await self.highrise.send_emote("dance-shoppingcart", user.id)
        if message.startswith("5"):
          await self.highrise.send_emote("dance-russian", user.id)
        if message.startswith("6"):
          await self.highrise.send_emote("idle_singing", user.id)
        if message.startswith("7"):
          await self.highrise.send_emote("idle-enthusiastic", user.id)   
        if message.startswith("8"):
          await self.highrise.send_emote("idle-dance-casual", user.id)   
        if message.startswith("9"):
          await self.highrise.send_emote("idle-loop-sitfloor", user.id)
        if message.startswith("10"):
          await self.highrise.send_emote("emote-lust", user.id)
        if message.startswith("11"):
          await self.highrise.send_emote("emote-greedy", user.id)
        if message.startswith("12"):
          await self.highrise.send_emote("emote-bow", user.id)
        if message.startswith("13"):
          await self.highrise.send_emote("emote-curtsy", user.id)
        if message.startswith("14"):
          await self.highrise.send_emote("emote-snowball", user.id)
        if message.startswith("15"):
          await self.highrise.send_emote("emote-snowangel", user.id)
        if message.startswith("16"):
          await self.highrise.send_emote("emote-confused", user.id)
        if message.startswith("17"):
          await self.highrise.send_emote("emote-teleporting", user.id)
        if message.startswith("18"):
          await self.highrise.send_emote("emote-swordfight", user.id)
        if message.startswith("19"):
          await self.highrise.send_emote("emote-energyball", user.id)
        if message.startswith("20"):
          await self.highrise.send_emote("dance-tiktok8", user.id)
        if message.startswith("21"):
          await self.highrise.send_emote("dance-blackpink", user.id)
        if message.startswith("22"):
          await self.highrise.send_emote("emote-model", user.id)
        if message.startswith("23"):
          await self.highrise.send_emote("dance-pennywise", user.id)
        if message.startswith("24"):
          await self.highrise.send_emote("dance-tiktok10", user.id)
        if message.startswith("25"):
          await self.highrise.send_emote("emote-telekinesis", user.id)
        if message.startswith("26"):
          await self.highrise.send_emote("emote-hot", user.id)
        if message.startswith("27"):
          await self.highrise.send_emote("dance-weird", user.id)
        if message.startswith("28"):
          await self.highrise.send_emote("emote-pose7", user.id)
        if message.startswith("29"):
          await self.highrise.send_emote("emote-pose8", user.id)
        if message.startswith("30"):
          await self.highrise.send_emote("emote-pose3", user.id)
        if message.startswith("31"):
          await self.highrise.send_emote("emote-pose5", user.id)  
        if message.startswith("32"):
          await self.highrise.send_emote("dance-employee", user.id)  
        if message.startswith("33"):
          await self.highrise.send_emote("emote-gift", user.id)  
        if message.startswith("34"):
          await self.highrise.send_emote("dance-touch", user.id)

        if message.startswith("35"):
          await self.highrise.send_emote("emote-creepycute", user.id)
        if message.startswith("36"):
          await self.highrise.send_emote("emote-iceskating", user.id)
        if message.startswith("37"):
          await self.highrise.send_emote("idle-wild", user.id)
        if message.startswith("38"):
          await self.highrise.send_emote("dance-kawai", user.id)
        if message.startswith("39"):
          await self.highrise.send_emote("dance-anime", user.id)
        if message.startswith("40"):
          await self.highrise.send_emote("emote-shy2", user.id)
        if message.startswith("41"):
          await self.highrise.send_emote("idle-uwu", user.id)  
        if message.startswith("42"):
          await self.highrise.send_emote("dance-wrong", user.id)  
        if message.startswith("43"):
          await self.highrise.send_emote("dance-icecream", user.id)  
        if message.startswith("44"):
          await self.highrise.send_emote("emote-fashionista", user.id)

        if message.startswith("45"):
          await self.highrise.send_emote("emote-punkguitar", user.id)
        if message.startswith("46"):
          await self.highrise.send_emote("emote-cutey", user.id)
        if message.startswith("47"):
          await self.highrise.send_emote("dance-weird", user.id)
        if message.startswith("48"):
          await self.highrise.send_emote("emote-cute", user.id)
        if message.startswith("49"):
          await self.highrise.send_emote("emote-energyball", user.id)
        if message.startswith("50"):
          await self.highrise.send_emote("emote-maniac", user.id)
        if message.startswith("51"):
          await self.highrise.send_emote("emote-sleigh", user.id)  
        if message.startswith("52"):
          await self.highrise.send_emote("dance-creepypuppet", user.id)  
        if message.startswith("53"):
          await self.highrise.send_emote("dance-pinguin", user.id)  
        if message.startswith("54"):
          await self.highrise.send_emote("emote-heartfingers", user.id)

        if message.startswith("55"):
          await self.highrise.send_emote("emote-timejump", user.id)
        if message.startswith("56"):
          await self.highrise.send_emote("emote-swordfight", user.id)
        if message.startswith("57"):
          await self.highrise.send_emote("emote-hearteyes", user.id)
        if message.startswith("58"):
          await self.highrise.send_emote("dance-zombie", user.id)
        if message.startswith("59"):
          await self.highrise.send_emote("emote-astronaut", user.id)
        if message.startswith("60"):
          await self.highrise.send_emote("idle-toilet", user.id)
        if message.startswith("61"):
          await self.highrise.send_emote("dance-jinglebell", user.id)  
        if message.startswith("62"):
          await self.highrise.send_emote("emote-hyped", user.id)  
        if message.startswith("63"):
          await self.highrise.send_emote("dance-blackpink", user.id)  
        if message.startswith("64"):
          await self.highrise.send_emote("emoji-gagging", user.id)

        if message.startswith("65"):
          await self.highrise.send_emote("emote-bow", user.id)
        if message.startswith("66"):
          await self.highrise.send_emote("emote-charging", user.id)
        if message.startswith("67"):
          await self.highrise.send_emote("emote-confused", user.id)
        if message.startswith("68"):
          await self.highrise.send_emote("emote-exasperatedb", user.id)
        if message.startswith("69"):
          await self.highrise.send_emote("emote-lust", user.id)
        if message.startswith("70"):
          await self.highrise.send_emote("emote-model", user.id)
        if message.startswith("71"):
          await self.highrise.send_emote("emote-snowangel", user.id)  
        if message.startswith("72"):
          await self.highrise.send_emote("emote-tired", user.id)  
        if message.startswith("73"):
          await self.highrise.send_emote("idle-enthusiastic", user.id)  
        if message.startswith("74"):
          await self.highrise.send_emote("dance-russian", user.id)



        if message.startswith("p1"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-float", roomUser.id)

        if message.startswith("p2"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-teleporting", roomUser.id)

        if message.startswith("p3"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-shy2", roomUser.id)



        if message.startswith("kawaii"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-kawai", roomUser.id)

        if message.startswith("p4"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-punkguitar", roomUser.id)



        if message.startswith("p5"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-jinglebell", roomUser.id)

        if message.startswith("p6"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-flex", roomUser.id)

        if message.startswith("p7"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-employee", roomUser.id)


        if message.startswith("p8"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-anime", roomUser.id)

        if message.startswith("p9"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-wild", roomUser.id)

        if message.startswith("p10"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-timejump", roomUser.id)



        if message.startswith("p11"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-iceskating", roomUser.id)

        if message.startswith("p12"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-touch", roomUser.id)

        if message.startswith("p13"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("sit-relaxed", roomUser.id)

        if message.startswith("p14"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-sleigh", roomUser.id)

        if message.startswith("p15"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hyped", roomUser.id)

        if message.startswith("p16"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-pinguin", roomUser.id)

        if message.startswith("p17"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-astronaut", roomUser.id)

        if message.startswith("p18"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-uwu", roomUser.id)

        if message.startswith("p19"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-tiktok4", roomUser.id)

        if message.startswith("p20"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-zombierun", roomUser.id)

        if message.startswith("p21"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-wrong", roomUser.id)

        if message.startswith("p22"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-tiktok9", roomUser.id)





        if message.startswith("p23"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-lust", roomUser.id)

        if message.startswith("p24"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-swordfight", roomUser.id)

        if message.startswith("p25"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle_singing", roomUser.id)

        if message.startswith("p26"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emoji-celebrate", roomUser.id)

        if message.startswith("p27"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("dance-weird", roomUser.id)

        if message.startswith("p28"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gravity", roomUser.id)



        if message.startswith("p29"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-creepycute", roomUser.id)

        if message.startswith("p30"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-frog", roomUser.id)

        if message.startswith("p31"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-gift", roomUser.id)

        if message.startswith("p32"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-boxer", roomUser.id)

        if message.startswith("p33"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-fashionista", roomUser.id)

        if message.startswith("p34"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-dance-casual", roomUser.id)

        if message.startswith("p35"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hearteyes", roomUser.id)

        if message.startswith("p36"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-exasperatedb", roomUser.id)

        if message.startswith("p37"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-enthusiastic", roomUser.id)

        if message.startswith("p38"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("emote-hot", roomUser.id)

        if message.startswith("p39"):
          if user.username.lower() in self.moderators:
            roomUsers = (await self.highrise.get_room_users()).content
            for roomUser, _ in roomUsers:
                await self.highrise.send_emote("idle-toilet", roomUser.id)


        if "Charging" in message:
          try:
            emote_id = "emote-charging"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Sing" in message:
          try:
            emote_id = "idle_singing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Wise" in message:
          try:
            emote_id = "dance-pennywise"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok2" in message:
          try:
            emote_id = "dance-tiktok2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Virgalrove" in message:
          try:
            emote_id = "dance-tiktok9"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Weird" in message:
          try:
            emote_id = "dance-weird"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Telekinesis" in message:
          try:
            emote_id = "emote-telekinesis"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok8" in message:
          try:
            emote_id = "dance-tiktok8"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Maniac" in message:
          try:
            emote_id = "emote-maniac"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Zombie" in message:
          try:
            emote_id = "emote-zombierun"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Relaxing" in message:
          try:
            emote_id = "emote-Relaxing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Gravity" in message:
          try:
            emote_id = "emote-gravity"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Fashon" in message:
          try:
            emote_id = "emote-fashionista"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Pose7" in message:
          try:
            emote_id = "emote-pose7"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Pink" in message:
          try:
            emote_id = "dance-blackpink"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Kiss" in message:
          try:
            emote_id = "emote-kiss"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Hello" in message:
          try:
            emote_id = "emote-hello"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Tiktok8" in message:
          try:
            emote_id = "dance-tiktok8"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Weird" in message:
          try:
            emote_id = "dance-weird"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")





        if "Model" in message:
          try:
            emote_id = "emote-model"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "no" in message:
          try:
            emote_id = "emote-no"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")



        if "Confused" in message:
          try:
            emote_id = "emote-confused"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "cute" in message:
          try:
            emote_id = "emote-cute"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Curtsy" in message:
          try:
            emote_id = "emote-curtsy"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Tiktok4 " in message:
          try:
            emote_id = "idle-dance-tiktok4"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Uwu" in message:
          try:
            emote_id = "idle-uwu"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print("error 3")

        if "Kpop" in message:
          try:
            emote_id = "dance-blackpink"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Energyball" in message:
          try:
            emote_id = "emote-energyball"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Float" in message:
          try:
            emote_id = "emote-float"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Frog" in message:
          try:
            emote_id = "emote-frog"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Teleport" in message:
          try:
            emote_id = "emote-teleporting"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sword" in message:
          try:
            emote_id = "emote-swordfight"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Casual" in message:
          try:
            emote_id = "idle-dance-casual"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Cutey" in message:
          try:
            emote_id = "idle-dance-cutey"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "You got a tip!" in message:
          try:
            emote_id = "dance-tiktok2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sing" in message:
          try:
            emote_id = "idle_singing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Greedy" in message:
          try:
            emote_id = "emote-greedy"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sweating" in message:
          try:
            emote_id = "emote-hot"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Pose1" in message:
          try:
            emote_id = "emote-superpose"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Russian dance" in message:
          try:
            emote_id = "dance-russian"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snake" in message:
          try:
            emote_id = "emote-snake"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Lust" in message:
          try:
            emote_id = "emote-lust"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Wise" in message:
          try:
            emote_id = "dance-pennywise"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Bow" in message:
          try:
            emote_id = "emote-bow"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Gagging" in message:
          try:
            emote_id = "emoji-gagging"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Rest" in message:
          try:
            emote_id = "idle-loop-sitfloor"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Enthused" in message:
          try:
            emote_id = "idle-enthusiastic"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snow ball" in message:
          try:
            emote_id = "emote-snowball"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Snow angel" in message:
          try:
            emote_id = "emote-snowangel"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Flex" in message:
          try:
            emote_id = "emoji-flex"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Laugh" in message:
          try:
            emote_id = "emote-laughing"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Yes" in message:
          try:
            emote_id = "emote-yes"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Guitar" in message:
          try:
            emote_id = "emote-punkguitar"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")



        if "Anime" in message:
          try:
            emote_id = "dance-anime"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Penguin" in message:
          try:
            emote_id = "dance-pinguin"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Airguitar " in message:
          try:
            emote_id = "idle-guitar"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Head" in message:
          try:
            emote_id = "emote-headblowup"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Creepy" in message:
          try:
            emote_id = "emote-creepycute"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sad" in message:
          try:
            emote_id = "emote-sad"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Zero" in message:
          try:
            emote_id = "emote-astronaut"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Sayso" in message:
          try:
            emote_id = "idle-dance-tiktok4"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")



        if "Shy" in message:
          try:
            emote_id = "emote-shy2"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Sleigh" in message:
          try:
            emote_id = "emote-sleigh"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Hyped" in message:
          try:
            emote_id = "emote-hyped"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Jingle" in message:
          try:
            emote_id = "dance-jinglebell"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Nervous" in message:
          try:
            emote_id = "idle-nervous"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")
        if "Timejump" in message:
          try:
            emote_id = "emote-timejump"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Skating" in message:
          try:
            emote_id = "dance-skating"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")

        if "Repose" in message:
          try:
            emote_id = "sit-relaxed"
            await self.highrise.send_emote(emote_id, user.id)
          except:
            print(f"{emote_id}")





        if message == "-coolboy":
          shirt = ["shirt-n_room12019buttondownblack"]
          pant = ["pants-n_room12019formalslacksblack"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018downturnedthinround', account_bound=False, active_palette=0),

                  Item(type='clothing', amount=1, id='hair_front-n_malenew20', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_malenew20', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malediamondsleepy', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_whitedans', account_bound=False, active_palette=0),


          ]) 
          await self.highrise.chat(f"good {xox}")


        if message == "-newdress":
          shirt = ["shirt-f_punklace"]
          pant = ["pants-n_room22019shortcutoffsdenim"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_01', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-basic2018openfullround', account_bound=False, active_palette=8),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2018straightpulledback', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018straightlonglowpigtails', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows14', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018pinkshadow2', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_whitedans', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='necklace-n_room32019locknecklace', account_bound=False, active_palette=-1),


                  Item(type='clothing', amount=1, id='earrings-n_room12019goldhoops', account_bound=False, active_palette=-1),


          ]) 
          await self.highrise.chat(f"good {xox}")

        if message.lower().startswith("/getoutfit"):
                response = await self.highrise.get_my_outfit()
                for item in response.outfit:
                    await self.highrise.chat(item.id)




        if message == "-dr":
          shirt = ["shirt-n_room12019cropsweaterblack"]
          pant = ["skirt-n_room12019pleatedskirtgrey"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='nose-n_basic2018newnose15', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id='mouth-n_room22019sillymouth', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=1, id='hair_front-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2020overshoulderwavy', account_bound=False, active_palette=1),

                  Item(type='clothing', amount=1, id='eyebrow-n_basic2018newbrows16', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018teardrop', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='shoes-n_registrationavatars2023gothgirlshoes', account_bound=False, active_palette=0),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle35', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle32', account_bound=False, active_palette=-1),



          ]) 
          await self.highrise.chat(f"good {xox}")

        if message == "-dress90":
          shirt = ["shirt-n_room32019longlineteesweatshirtgrey"]
          pant = ["pants-n_starteritems2019cuffedjeansblue"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=4),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=4, id='hair_back-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),

                  Item(type='clothing', amount=4, id='hair_front-n_malenew19', account_bound=False, active_palette=80),
                  Item(type='clothing', amount=1, id='watch-n_room32019blackwatch', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_room12019sneakersblack', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018whistlemouth', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018malealmondsquint', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_04', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")

        if message == "-dress56":
          shirt = ["shirt-n_starteritems2019femtshirtwhite"]
          pant = ["skirt-n_starteritems2018whiteskirt"]
          item_top = random.choice(shirt)
          item_bottom = random.choice(pant)
          xox = await self.highrise.set_outfit(outfit=[
                  Item(type='clothing', amount=1, id='body-flesh', account_bound=False, active_palette=23),
                  Item(type='clothing', amount=1, id=item_top, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id=item_bottom, account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_back-n_basic2018wavymed', account_bound=False, active_palette=39),
                  Item(type='clothing', amount=1, id='nose-n_basic2018newnose04', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='hair_front-n_basic2019wavyflipdroop', account_bound=False, active_palette=39),

                  Item(type='clothing', amount=1, id='freckle-n_basic2018freckle22', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='blush-n_salonshop2018blush', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='sock-n_starteritems2020whitesocks', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='shoes-n_starteritems2018conversewhite', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='mouth-basic2018fullround', account_bound=False, active_palette=-1),
                  Item(type='clothing', amount=1, id='eye-n_basic2018dolleyes', account_bound=False, active_palette=7),
                  Item(type='clothing', amount=1, id='eyebrow-n_08', account_bound=False, active_palette=-1),

          ])
          await self.highrise.chat(f"{xox}")







        if message.lower().lstrip().startswith(("!modcommands", "-mod", "-modcommands", "!mod", "mods")) and user.username in moderators:
           await self.highrise.send_whisper(user.id, f"<#990066>sure 🫶🏻\n!ban @name\n !mute @name\n !kick @name\n !unmute @name\n !heart @name number\n !go @name\n !tp @name\n ❤️ all\n p1 ...... p39 to emote all")
           await self.highrise.send_whisper(user.id, f"<#990066>!wallet\n !buyboost\n !buyvoice\n !vip\n !vip @naame\n !promote @name moderator or designer\n !demote @name moderator or designer\n!follow @name \n !stop to stop it")






        if message.startswith("!tp") and user.username in moderators:
           target_username = message.split("@")[-1].strip()
           if target_username not in ["", ""]:
              await self.teleport_user_next_to(target_username, user)


        if message.startswith("!go") and user.username in moderators:
           target_username = message.split("@")[-1].strip()
           if target_username not in ["", ""]:
              await self.teleport_requester_to_user(target_username, user)




        if message.startswith("promote"):
            if user.username in moderators:
                await self.highrise.chat("You do not have permission to use this command.")

                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid promote command format.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), True)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been promoted to {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return

        if message.startswith("demote"):
            if user.username != "DeaJy":
                await self.highrise.chat("You do not have permission to use this command.")
                return
            parts = message.split()
            if len(parts) != 3:
                await self.highrise.chat("Invalid demote command format.")
                return
            command, username, role = parts
            if "@" not in username:
                username = username
            else:
                username = username[1:]
            if role.lower() not in ["moderator", "designer"]:
                await self.highrise.chat("Invalid role, please specify a valid role.")
                return
            #check if user is in room
            room_users = (await self.highrise.get_room_users()).content
            for room_user, pos in room_users:
                if room_user.username.lower() == username.lower():
                    user_id = room_user.id
                    break
            if "user_id" not in locals():
                await self.highrise.chat("User not found, please specify a valid user and coordinate")
                return
            #promote user
            permissions = (await self.highrise.get_room_privilege(user_id))
            setattr(permissions, role.lower(), False)
            try:
                await self.highrise.change_room_privilege(user_id, permissions)
                await self.highrise.chat(f"{username} has been demoted from {role}.")
            except Exception as e:
                await self.highrise.chat(f"Error: {e}")
                return    

        if "موتي" in message or "سنه موتي" in message:
            death_year = random.randint(2024, 2100)
            await self.highrise.chat(f" {user.username} الصراح معرفش امتي هتموت بس اعتقد {death_year}")

        if "نسبه الذكاء" in message or "الذكاء" in message:
            iq = random.randint(0, 100)
            if iq <= 10:
               await self.highrise.chat(f" @{user.username} نسبه ذكاءك {iq}% ,صحبي انت غبي ")
            elif iq >= 90:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,You are clever than most of other dumb in this room")
            elif iq >10 and iq <90:              
               await self.highrise.chat(f" ( {user.username} ) نسبه ذكائك : {iq}%")

        if "الحب" in message or "نسبه الحب" in message:
            love_percentage = random.randint(0, 100)
            if love_percentage == 100:
                await self.highrise.chat(f" {user.username} {love_percentage}% الكل بيحيك")
            elif love_percentage == 0:
                await self.highrise.chat(f" {user.username} {love_percentage}% مفيش حد بسجبك روح عيط ")
            elif love_percentage <100 or love_percentage >0:
                await self.highrise.chat(f" {user.username} فقط {love_percentage}% بس الناس بتحبك!!")

        if "نسبه الكره" in message or "الكره" in message:
            hate_percentage = random.randint(0, 100)
            if hate_percentage == 0:
                await self.highrise.chat(f" {user.username} {hate_percentage}% مفيش حد بيكرهك")
            elif hate_percentage == 100:
                await self.highrise.chat(f" {user.username} {hate_percentage}% الك بيكرهك اجري عيط ")
            elif hate_percentage < 100 or hate_percentage > 0:
                await self.highrise.chat(f" {user.username} بس {hate_percentage}% الناس بتكرهك")

        if "Deathyear" in message or "deathyear" in message:
            death_year = random.randint(2023, 2100)
            await self.highrise.chat(f" {user.username} IDK when you would die but maybe around: {death_year}")

        if "Iq" in message or "iq" in message:
            iq = random.randint(0, 100)
            if iq <= 10:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,Bro you are dumb asf ,lol ")
            elif iq >= 90:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,You are clever than most of other dumb in this room")
            elif iq >10 and iq <90:              
               await self.highrise.chat(f"Your ( {user.username} ) iq is : {iq}%")

        if "Lovepercentage" in message or "lovepercentage" in message:
            love_percentage = random.randint(0, 100)
            if love_percentage == 100:
                await self.highrise.chat(f" {user.username} {love_percentage}% Everyone loves ya")
            elif love_percentage == 0:
                await self.highrise.chat(f" {user.username} {love_percentage}% No one loves ya,Go cry in that corner ")
            elif love_percentage <100 or love_percentage >0:
                await self.highrise.chat(f" {user.username} Only {love_percentage}% People loves ya!!")

        if "Hatepercentage" in message or "hatepercentage" in message:
            hate_percentage = random.randint(0, 100)
            if hate_percentage == 0:
                await self.highrise.chat(f" {user.username} {hate_percentage}% No one hates ya")
            elif hate_percentage == 100:
                await self.highrise.chat(f" {user.username} {hate_percentage}% Everyone hates ya,Go cry in that corner ")
            elif hate_percentage < 100 or hate_percentage > 0:
                await self.highrise.chat(f" {user.username} Only {hate_percentage}% people hates ya")

        if "Straightmeter" in message or "straightmeter" in message:
            straight_metre = random.randint(0,100)
            if straight_metre <=10:
                await self.highrise.chat(f"{user.username} {straight_metre}% Why are you Gay?? ")
            elif straight_metre <50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  YOU ARE GAY!!!")
            elif straight_metre ==50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  OMG,YOU ARE Bi!!!")
            elif straight_metre <=90:
                await self.highrise.chat(f"{user.username} {straight_metre}%  You are normal ")
            elif straight_metre >=90  :
                await self.highrise.chat(f"{user.username} {straight_metre}% You are straighter than my programming code ")



    async def send_continuous_emote(self, emote_text ,user_id,emote_time):
      try:
          while True:                    
                tasks = [asyncio.create_task(self.highrise.send_emote(emote_text, user_id))]
                await asyncio.wait(tasks)
                await asyncio.sleep(emote_time)
                await asyncio.sleep(1)
      except Exception as e:
                print(f"{e}")


    async def stop_continuous_emote(self, user_id: int):
      if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
          task = self.continuous_emote_tasks[user_id]
          task.cancel()
          with contextlib.suppress(asyncio.CancelledError):
              await task
          del self.continuous_emote_tasks[user_id]

    async def follow_user(self, target_username: str):
      while self.following_username == target_username:

          response = await self.highrise.get_room_users()
          target_user_position = None
          for user_info in response.content:
              if user_info[0].username.lower() == target_username.lower():
                  target_user_position = user_info[1]
                  break

          if target_user_position:
              nearby_position = Position(target_user_position.x + 1.0, target_user_position.y, target_user_position.z)
              await self.highrise.walk_to(nearby_position)

              await asyncio.sleep(2)
    async def get_emote_E(self, target) -> None: 

     try:
        emote_info = self.Emotes.get(target)
        return emote_info
     except ValueError:
        pass
    async def on_whisper(self, user: User, message: str ) -> None:

        if message == "here":
            if user.username.lower() in self.moderators:
                response = await self.highrise.get_room_users()
                users = [content for content in response.content]
                for u in users:
                    if u[0].id == user.id:
                        try:
                            await self.highrise.teleport(Counter.bot_id,Position((u[1].x),(u[1].y),(u[1].z),"FrontRight"))


                            break
                        except:

                            pass

        if message.startswith("/say"):
            if user.username.lower() in self.moderators:
                text = message.replace("/say", "").strip()
                await self.highrise.chat(text)




        elif message.startswith("/come"):
            if user.username.lower() in self.moderators:
                response = await self.highrise.get_room_users()
                your_pos = None
                for content in response.content:
                    if content[0].id == user.id:
                        if isinstance(content[1], Position):
                            your_pos = content[1]
                            break
                if not your_pos:
                    await self.highrise.send_whisper(user.id, "Invalid coordinates!")
                    return
                await self.highrise.chat(f"@{user.username} I'm coming ..")
                await self.highrise.walk_to(your_pos)

        elif message.lower().startswith("/follow"):

            target_username = message.split("@")[1].strip()

            if target_username.lower() == self.following_username:
                await self.highrise.send_whisper(user.id,"I am already following.")
            elif message.startswith("/say"):
              if user.username.lower() in self.moderators:
                  text = message.replace("/say", "").strip()
                  await self.highrise.chat(text)
            else:
                self.following_username = target_username
                await self.highrise.chat(f"hey {target_username}.")

                await self.follow_user(target_username)
        elif message.lower() == "stop following":
            self.following_username = None

            await self.highrise.walk_to(Position(16,0,1.5,"FrontLeft"))


    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem) -> None:

          print(f"NOW IS VIP {sender.username}")
          if receiver.username == "CheetahBot" :
            if tip.amount == 100 :
              await self.highrise.teleport(f"{sender.id}", Position(x=17.0, y=8.75, z=18.0, facing='FrontLeft'))
              await self.highrise.chat(f"NOW IS VIP {sender.username}")
          if receiver.username == "CheetahBot" :
            if tip.amount == 500 :
              await self.highrise.teleport(f"{sender.id}", Position(x=17.0, y=8.75, z=18.0, facing='FrontLeft'))
              await self.highrise.chat(f"𝑪𝒐𝒏𝒈𝒓𝒂𝒕𝒖𝒍𝒂𝒕𝒊𝒐𝒏𝒔 𝑵𝒐𝒘 𝑽𝑰𝑷 {sender.username} AMOUNT OF {tip.amount}G")


          if receiver.username == "CheetahBot" :
            if tip.amount == 1000 :
              await self.highrise.teleport(f"{sender.id}", Position(x=17.0, y=8.75, z=18.0, facing='FrontLeft'))
              await self.highrise.chat(f"𝑪𝒐𝒏𝒈𝒓𝒂𝒕𝒖𝒍𝒂𝒕𝒊𝒐𝒏𝒔 𝑵𝒐𝒘 𝑽𝑰𝑷 {sender.username} AMOUNT OF {tip.amount}G")


          if receiver.username == "CheetahBot" :
            if tip.amount == 5000 :
              await self.highrise.teleport(f"{sender.id}", Position(x=17.0, y=8.75, z=18.0, facing='FrontLeft'))
              await self.highrise.chat(f"𝑪𝒐𝒏𝒈𝒓𝒂𝒕𝒖𝒍𝒂𝒕𝒊𝒐𝒏𝒔 𝑵𝒐𝒘 𝑽𝑰𝑷 {sender.username} AMOUNT OF {tip.amount}G")


          if receiver.username == "CheetahBot" :
            if tip.amount == 10000 :
              await self.highrise.teleport(f"{sender.id}", Position(x=17.0, y=8.75, z=18.0, facing='FrontLeft'))
              await self.highrise.chat(f"𝑪𝒐𝒏𝒈𝒓𝒂𝒕𝒖𝒍𝒂𝒕𝒊𝒐𝒏𝒔 𝑵𝒐𝒘 𝑽𝑰𝑷 {sender.username} AMOUNT OF {tip.amount}G")

    async def on_user_join(self, user: User, position: Position | AnchorPosition) -> None:

      if user.username == "DEMON_EJ_11":
        await self.highrise.chat("<#FF3300>hello Mr.EJ nice to see ya❤️‍🔥")

      elif user.username in mods:
        await self.highrise.chat(f"<#FF0000>mod @{user.username} join the room")

      elif user.username == "tomyHR":
        await self.highrise.chat("<#FF3300>Designer bot @tomyHR here now")

        return  # This exits the function if tomyHR is greeted
      else:
        message = random.choice([f"<#dd0339>Hi Welcome @{user.username} To Find a diamond! This Is Where You Hang Out, Talk, And Maybe Find The One, Invite Your Friends :) ! Pls Leave Feedbacks, Have Fun! Go Mingle!"])
        await self.highrise.chat(f"{message}")

    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:

        response = await self.highrise.get_messages(conversation_id)
        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            message = response.messages[0].content
            print (message)
        if message.lower().lstrip().startswith(("hello","hi","ello","hello bot","hi bot","ello bot")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"𝙃𝙚𝙡𝙡𝙤 𝙝𝙣 ")

        if message.lower().lstrip().startswith(("!modcommands","!mod")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"<#990066>sure 🫶🏻\n!ban @name\n  !mute @name\n !kick @name\n !unmute @name\n ❤️ @name number\n !go @name\n !tp @name\n ❤️ all\n p1 ...... p39 to emote all\n !wallet\n !userinfo @name\n !buyboost\n !buyvoice")



        if message.lower().lstrip().startswith(("!commands","!list commands")):
            await asyncio.sleep(2)
            await self.highrise.send_message(conversation_id, f"<#990066>sure 🫶🏻\nloop number\nstop to stop loop\n emote @name\n write any number to get emote\n lovepercentage\n hatepercentage\n deathyear \n joke\n Rizz\n")





    async def on_user_move(self, user: User, pos: Position | AnchorPosition) -> None:
      if user.username == "tomyHR":
         print(f"{user.username}: {pos}")
      if user:

        if self.dance_floor_pos:

            if isinstance(pos, Position):

                for dance_floor_info in self.dance_floor_pos:

                    if (
                        dance_floor_info[0] <= pos.x <= dance_floor_info[1] and
                        dance_floor_info[2] <= pos.y <= dance_floor_info[3] and
                        dance_floor_info[4] <= pos.z <= dance_floor_info[5]
                    ):

                        if user.id not in self.dancer:
                            self.dancer.append(user.id)

                        return

            # If not in any dance floor area
            if user.id in self.dancer:
                self.dancer.remove(user.id)



        print(f"{user.username}: {pos}")



