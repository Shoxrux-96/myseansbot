import asyncio
import os
from telethon.sync import TelegramClient

API_ID = int(input("API ID ni kiriting: "))
API_HASH = input("API HASH ni kiriting: ")
SESSION_NAME = input("Yaratilayotgan sessiya nomini kiriting (masalan: my_account): ")

async def main():
    async with TelegramClient(SESSION_NAME, API_ID, API_HASH) as client:
        print("Muvaffaqiyatli ulandi. Sessiya fayli yaratildi.")

if __name__ == "__main__":
    asyncio.run(main())
