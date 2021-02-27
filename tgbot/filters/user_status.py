from aiogram import Dispatcher
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from aiogram.types.base import TelegramObject

class AdminFilter(BoundFilter):
    key = 'is_admin'

    def __init__(self, is_admin: bool):
        self.is_admin = is_admin

    async def check(self, obj: TelegramObject):
        data = ctx_data.get()
        user = data["user"]
        return (user.is_admin()) == self.is_admin

def setup(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)