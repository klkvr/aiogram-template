from aiogram import Dispatcher

from . import user_status

def setup(dp: Dispatcher):
    user_status.setup(dp)