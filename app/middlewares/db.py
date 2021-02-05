from aiogram.dispatcher.middlewares import LifetimeControllerMiddleware
from aiogram import Dispatcher

from app.models.user import BotUser


class DbMiddleware(LifetimeControllerMiddleware):
    def __init__(self):
        super().__init__()

    async def pre_process(self, obj, data, *args):
        if not hasattr(obj, "from_user"):
            data["user"] = None
        elif obj.from_user == None:
            data["user"] = None
        else:
            data["user"] = BotUser(obj.from_user.id)

    async def post_process(self, obj, data, *args):
        del data["user"]

def setup(dp: Dispatcher):
    dp.middleware.setup(DbMiddleware())