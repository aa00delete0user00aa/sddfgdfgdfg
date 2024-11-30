import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='7669581824:AAHgxatHQ1Dv0oJnHJeGemo--1c1O0haEkw')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
print('fhgfh')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')