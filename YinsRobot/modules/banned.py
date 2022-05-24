# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @AyiinXd

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from YinsRobot.events import register


@register(pattern="^/banall(?: |$)(.*)")
async def testing(ayiinxd):
    ayiin = await ayiinxd.get_chat()
    yins = await ayiinxd.client.get_me()
    admin = ayiin.admin_rights
    creator = ayiin.creator
    if not admin and not creator:
        await ayiinxd.reply(f"**Maaf {yins.first_name} Bukan admin...**")
        return
    xnxx = await ayiinxd.reply("Processing...")
# Thank for Dark_Cobra
    ayiinkontol = await ayiinxd.client.get_participants(ayiinxd.chat_id)
    for user in ayiinkontol:
        if user.id == yins.id:
            pass
        try:
            xx = await bot(EditBannedRequest(ayiinxd.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await xnxx.edit(f"Kesalahan: {str(e)}")
        await sleep(.5)
    await xnxx.edit("Tidak melakukan apa-apa")
