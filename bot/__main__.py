import asyncio
import json
import logging
import os

import time
import socket

from .bot import BoilerplateDiscordBot

async def run():
    bot = BoilerplateDiscordBot()
    try:
        token = os.getenv('DISCORD_BOT_TOKEN')
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.set_debug(False)
    loop.run_until_complete(run())
