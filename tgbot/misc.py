from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.redis import RedisStorage2
import redis

from app import config


main_redis_db = redis.Redis(host=config.REDIS_HOST, db=config.MAIN_REDIS_DB, decode_responses=True)
bot = Bot(config.BOT_HASH)
storage = RedisStorage2(host=config.REDIS_HOST, db=config.MAIN_REDIS_DB)
dp = Dispatcher(bot, storage=storage)

def setup():
    from app import filters
    from app import middlewares

    middlewares.setup(dp)
    filters.setup(dp)
    from app import handlers