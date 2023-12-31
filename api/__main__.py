import asyncio
import sys
import logging
import logging.handlers as handlers
from pyrogram import idle
from aiohttp import web
from api.vars import Var
# from Bot.bot import TGBot
from api.server import web_server

logging.basicConfig(
    level=logging.INFO,
    datefmt="%d/%m/%Y %H:%M:%S",
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(stream=sys.stdout),
              handlers.RotatingFileHandler("logfile.log", mode="a", maxBytes=104857600, backupCount=2, encoding="utf-8")],)

logging.getLogger("aiohttp").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp.web").setLevel(logging.ERROR)

server = web.AppRunner(web_server())

loop = asyncio.get_event_loop()

async def main():
    # logging.info("Starting Bot")
    # await TGBot.start()
    logging.info("Initalizing Web Server")
    await server.setup()
    bind_address = Var.BIND_ADDRESS
    await web.TCPSite(server, bind_address, Var.PORT).start()
    logging.info("DONE")
    logging.info(f"API running on {Var.URL}")

    # await idle()
if __name__ == "__main__":
    try:
        loop.run_until_complete(main())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        logging.error(err.with_traceback(None))
    finally:
        loop.stop()
        logging.info("Stoped API")