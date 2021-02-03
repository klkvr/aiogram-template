import redis
import json

from app.misc import main_redis_db
from .db import DbClass
from app import config

class BotUser(DbClass):
    db = main_redis_db
    db_name = 'user'
    attrs = [{'name': 'started', 'default': False},
    ]
    ignored_attrs = []

    def is_admin(self):
        return self.id in config.ADMINS