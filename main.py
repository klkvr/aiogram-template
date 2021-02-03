from app import misc
from aiogram import executor

misc.setup()

if __name__ == '__main__':
    executor.start_polling(misc.dp, skip_updates=False)