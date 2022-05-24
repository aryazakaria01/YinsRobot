# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @AyiinXd

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from telegram.error import BadRequest
from telegram.ext import CallbackContext, Filters, CommandHandler, run_async, CallbackQueryHandler
from telegram.utils.helpers import mention_html
from typing import Optional, List
from telegram import TelegramError

from YinsRobot.modules.helper_funcs.chat_status import bot_admin, dev_plus
from YinsRobot import DEV_USERS, dispatcher

from telegram.ext import CallbackContext, run_async

@bot_admin
@dev_plus
def banall(update: Update, context: CallbackContext):
    chat = update.effective_chat
    bot = context.bot
    yins = bot.get_me()
    admin = update.admin_rights
    creator = update.creator
    if not admin and not creator:
        update.effective_message.reply_text(f"**Maaf {yins.first_name} Bukan admin...**")
        return
    elif DEV_USERS:
        update.effective_message.reply_text("Processing...")
    # Thank for Dark_Cobra
    ayiinkontol = bot.get_participants(chat)
    for user in ayiinkontol:
        if user.id == yins.id:
            pass
        try:
         bot(EditBannedRequest(ayiinxd.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await xnxx.edit(f"Kesalahan: {str(e)}")
        await sleep(.5)
    update.effective_message.reply_text("Tidak melakukan apa-apa")


BANALL_HANDLER = CommandHandler("banall", banall, run_async=True)

dispatcher.add_handler(BANALL_HANDLER)

__handlers__ = [
    BANALL_HANDLER,
]
