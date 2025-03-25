import os
import time
import asyncio
from binance.client import Client
from telegram import Bot

# Отримуємо API-ключі з змінних середовища (для безпеки)
API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

#Перевіряємо, чи 
# Підключаємо Binance API
client = Client(API_KEY, SECRET_KEY)

# Підключаємо Telegram бота
bot = Bot(token=TELEGRAM_BOT_TOKEN)

async def send_telegram_message(message):
    """ Асинхронна відправка повідомлення в Telegram """
    await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

def find_triangular_arbitrage():
    """ Функція пошуку трикутного арбітражу """
    tickers = client.get_all_tickers()
    
    # Тут має бути логіка пошуку арбітражних можливостей
    # Наприклад, купити BTC за USDT, продати BTC за ETH, потім ETH → USDT
    
    profit = 1.5  # Припустимо, знайшли угоду з 1.5% прибутку
    if profit > 1:
        message = f"Знайдено арбітраж! Прибуток: {profit}%"
        await asyncio.run(send_telegram_message(message))

async def main():
    while True:
    find_triangular_arbitrage()
    await asyncio.sleep(10)  # Запускаємо перевірку кожні 10 секунд

if __name__ == "__main__":
    asyncio.run(main())