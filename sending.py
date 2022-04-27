from telethon import TelegramClient
import asyncio
from telethon.sessions import StringSession
import time

import os
import requests
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty

import asyncio
import io
from telethon.utils import get_display_name
from __init__ import send,intervel

api_hash=os.environ.get("API_HASH", False)
api_id=os.environ.get("API_ID", False)
string =os.environ.get("SESSION", False)

async def sending():
    async with TelegramClient(StringSession(string), api_id, api_hash) as client:
        await client.start()
        message = await client.send_message("me", 'Sending...')
        dialog_count = 500
        stime=intervel()
        entities = await client.get_dialogs(dialog_count)
        previous_message=send()
        if previous_message:
            error_count = 0
            sent_count = 0
            for pro in range(0,24,1):
                for i, entity in enumerate(entities):
                    i += 1  # 1-based index
                    if len(str(entity.id))>=10:
                        if len(str(entity.id))==10:
                            group=int("-100"+str(entity.id))
                            try:
                                await client.send_message(group, previous_message)
                                sent_count += 1
                                await client.edit_message("me",message,
                                f"Sent : {sent_count}\nError : {error_count}",
                                )
                            except Exception as error:
                                await client.send_message(
                                "me",
                                f"Error in sending at {entity.id}.\n\n{error}",
                                )
                                error_count += 1
                                await client.edit_message("me",message,
                                    f"Sent : {sent_count}\nError : {error_count}",
                                )
                        else:
                            try:
                                await client.send_message(entity.id, previous_message)
                                sent_count += 1
                                await client.edit_message("me",message,
                                f"Sent : {sent_count}\nError : {error_count}",
                                )
                            except Exception as error:
                                
                                    await client.send_message(
                                    "me",
                                    f"Error in sending at {entity.id}.\n\n{error}",
                                )
                                    error_count += 1
                                    await client.edit_message("me",message,
                                        f"Sent : {sent_count}\nError : {error_count}",
                                    )
                if error_count > 0:
                    await client.send_message(
                        "me",
                        f"{error_count} Errors",)
                ttime=float(stime)*3600
                await asyncio.sleep(ttime)
