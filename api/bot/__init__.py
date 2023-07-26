import logging
from pyrogram import Client
from api.vars import Var

TGBot=Client(
    "Bot_session",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    workdir="Bot",
    )