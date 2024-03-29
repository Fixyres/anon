from telethon import TelegramClient, events
import random

api_id = '20045757'
api_hash = '7d3ea0c0d4725498789bd51a9ee02421'

bot = TelegramClient('anonimka', api_id, api_hash)

AtlPidor = ["Ну давай давай напиши 😡", "Кхм кхм 📨", "Кто ты\n🤔🤔🤔", "Атл лох кста 🤥", "🤫🧏‍♂️"]

@bot.on(events.NewMessage(pattern='/anonimka'))
async def handler(event):
    HuySani = random.choice(AtlPidor)
    await event.reply(f'{HuySani}\nt.me/letsqbot?start=kcPnoX')

with bot:
    bot.run_until_disconnected()
