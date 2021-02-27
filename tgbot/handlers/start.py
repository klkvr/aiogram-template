from aiogram.types import Message

from app.misc import dp
from app.templates import messages
from app.models.user import BotUser

@dp.message_handler(commands=['start'])
async def start_cmd(m: Message, user: BotUser):
    user.started = True
    await m.answer(messages.START)