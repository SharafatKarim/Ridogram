from ciraag.core.module_injector import *
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import SetTypingRequest
from telethon.types import SendMessageTypingAction
from random import choice
from ciraag.docs.slangs import hindi_slangs

user_opponent = set([])
ciraag_user = int(environ["owner_id"])

class Opponent:
    async def set_opponent(self, event):
        self.find_user = await event.get_reply_message()
        self.user_id = self.find_user.sender_id
        self.chat = event.to_id
        self.message = await event.get_reply_message()
        self.reply = self.message.id
        self.get_first_name = await ciraag(GetFullUserRequest(self.user_id))
        self.first_name = self.get_first_name.users[0].first_name
        if self.user_id not in user_opponent:
            user_opponent.add(self.user_id)
            await ciraag.send_message(self.chat, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> Bound within Ciraag's sight, your forehead is condemned to become a horrifying scroll, upon which your doom shall be inscribed.", reply_to=self.reply, parse_mode="html")
        else:
            await ciraag.send_message(self.chat, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> This opponent has already been sent deep into the hellish prison of Ciraag.", reply_to=self.reply, parse_mode="html")

    async def remove_opponent(self, event):
        self.find_user = await event.get_reply_message()
        self.user_id = self.find_user.sender_id
        self.chat = event.to_id
        self.message = await event.get_reply_message()
        self.reply = self.message.id
        self.get_first_name = await ciraag(GetFullUserRequest(self.user_id))
        self.first_name = self.get_first_name.users[0].first_name
        if self.user_id in user_opponent:
            user_opponent.remove(self.user_id)
            await ciraag.send_message(self.chat, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> Released from the shackles of a life led by Ciraag's frightening gaze.", reply_to=self.reply, parse_mode="html")
        else:
            await ciraag.send_message(self.chat, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> This user has already been released from Ciraag's jail.", reply_to=self.reply, parse_mode="html")

    async def fighter_genie(self, event):
        if event.is_private:
            self.user_id = event.peer_id.user_id
            await ciraag(SetTypingRequest(self.user_id, SendMessageTypingAction()))
            self.sender = await event.get_sender()
            self.sender_id = self.sender.id
            self.reply = event.id
            if user_opponent:
                if self.user_id in user_opponent:
                    if self.sender_id == ciraag_user:
                        pass
                    else:
                        self.get_first_name = await ciraag(GetFullUserRequest(self.user_id))
                        self.first_name = self.get_first_name.users[0].first_name
                        self.random_hindi_slangs = choice(hindi_slangs)
                        await ciraag.send_message(self.user_id, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> {self.random_hindi_slangs}", reply_to=self.reply, parse_mode="html")
        elif event.is_group:
            self.chat = event.to_id
            await ciraag(SetTypingRequest(self.chat, SendMessageTypingAction()))
            self.user_id = event.from_id.user_id
            self.sender = await event.get_sender()
            self.sender_id = self.sender.id
            self.reply = event.id
            if user_opponent:
                if self.user_id in user_opponent:
                    if self.sender_id == ciraag_user:
                        pass
                    else:
                        self.get_first_name = await ciraag(GetFullUserRequest(self.user_id))
                        self.first_name = self.get_first_name.users[0].first_name
                        self.random_hindi_slangs = choice(hindi_slangs)
                        await ciraag.send_message(self.chat, f"<a href='tg://user?id={self.user_id}'>{self.first_name}</a> {self.random_hindi_slangs}", reply_to=self.reply, parse_mode="html")