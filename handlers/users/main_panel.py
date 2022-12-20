from aiogram import F, Router
from aiogram.types import Message

from keyboards.reply.users import main_panel

user_main_router = Router(name='user_main_panel')


@user_main_router.message(F.text == '/start')
async def command_start(message: Message):
    await message.delete()
    await message.answer(
        text='ДОБРО ПОЖАЛОВАТЬ!',
        reply_markup=main_panel
    )
