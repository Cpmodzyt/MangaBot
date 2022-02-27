import asyncio as aio
from bot import bot
from models import DB


async def async_main():
    db = DB()
    await db.connect()

if __name__ == '__main__':
    loop = aio.new_event_loop()
    loop.run_until_complete(async_main())
    bot.run()

