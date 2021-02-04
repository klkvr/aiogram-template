import redis
import json

class DbClass:
    def __init__(self, id):
        self.id = id
        self.ignored_attrs.extend(['id', 'db', 'db_name'])
        for attr in self.attrs:
            if self.db.exists(f'{self.db_name}:{self.id}:{attr["name"]}'):
                self.__dict__[attr["name"]] = json.loads(self.db.get(f'{self.db_name}:{self.id}:{attr["name"]}'))
            else:
                self.__dict__[attr["name"]] = attr["default"]
    
    def __setattr__(self, name, value):
        if name in self.ignored_attrs:
            self.__dict__[name] = value
        else:
            self.__dict__[name] = value
            self.db.set(f'{self.db_name}:{self.id}:{name}', json.dumps(value))