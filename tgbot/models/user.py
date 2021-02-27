import redis
import json
from aiogram.types.base import TelegramObject
from aiogram.utils.markdown import quote_html

from app.misc import main_redis_db
from .db import DbClass
from app import config

class BotUser(DbClass):
    db = main_redis_db
    db_name = 'user'
    attrs = [
            {'name': 'tg_name', 'default': None},
            {'name': 'tg_username', 'default': None},
    ]
    ignored_attrs = []

    def is_admin(self):
        return self.id in config.ADMINS
    
    def did_something(self, obj: TelegramObject):
        if hasattr(obj, "from_user"):
            self.tg_name = obj.from_user.full_name
            if obj.from_user.username is not None:
                self.tg_username = obj.from_user.username.lower()
    
    def get_link(self):
        return f"<a href='tg://user?id={self.id}'>"\
                    f"{quote_html(f'@{self.tg_username}' if self.tg_username != None else self.tg_name)}</a>"