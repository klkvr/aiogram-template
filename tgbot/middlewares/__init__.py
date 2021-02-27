from . import db
from aiogram import Dispatcher

def setup(dp: Dispatcher):
    db.setup(dp)