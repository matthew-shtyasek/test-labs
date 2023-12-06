import asyncio

from aiogram import Bot, Dispatcher
from root_menu import router as main_router
from lab1.routing import router as lab1_router
from lab2.routing import router as lab2_router
from lab3.routing import router as lab3_router
from lab4.routing import router as lab4_router
from lab5.routing import router as lab5_router
from lab6.routing import router as lab6_router
from lab7.routing import router as lab7_router


BOT_TOKEN = '6391231821:AAH-79HJxcjiwLti7pIXurtEVYQ8ZNAwj58'

dp = Dispatcher()
dp.include_router(main_router)
dp.include_router(lab1_router)
dp.include_router(lab2_router)
dp.include_router(lab3_router)
dp.include_router(lab4_router)
dp.include_router(lab5_router)
dp.include_router(lab6_router)
dp.include_router(lab7_router)


async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
