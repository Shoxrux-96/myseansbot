from telethon import TelegramClient, events
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ai_handler import ask_ai
from admin.database import insert_message


api_id = 20270979
api_hash = '75e62ce7bb9233884c955d4432140f1f'
session_name = 'Shoxrux.session'

bot = TelegramClient(session_name, api_id, api_hash)

@bot.on(events.NewMessage)
async def handle_message(event):
    sender = await event.get_sender()
    username = sender.username or "NoUsername"
    name = sender.first_name or "Anon"
    text = event.raw_text

    # AI javob olish
    ai_reply = ask_ai(text)

    # Javob berish
    await event.reply(ai_reply)

    # Ma'lumotni bazaga yozish
    insert_message(sender.id, name, username, text, ai_reply)

bot.start()
bot.run_until_disconnected()
