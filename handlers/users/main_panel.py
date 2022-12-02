from aiogram import Router, F
from aiogram.types import Message, CallbackQuery


from gen import UserCallbackData
from models import User
from keyboards.reply import user_panel
from keyboards.inline import keyboard

from models.models import Categories

user_main_panel = Router(name='user_main_panel')


# @user_main_panel.message(F.text == '/st ')
# async def sf(message: Message):
#     await message.delete()
#     if await Categories.get(pk=message.from_user.id):
#         await message.answer(text='каталог т2', reply_markup=await keyboard())
#     else:
#         user = Categories(id=message.from_user, name=message.from_user)
#         await user.save()
#         await message.answer(text='Зарегистрирован.', reply_markup=await keyboard())
#
#
# @user_main_panel.callback_query(UserCallbackData.filter((F.target == 'nok') & (F.action == 'get')))
# async def user_man(callback: CallbackQuery):
#     await callback.message.edit_text(
#         text='выберите товар',
#         reply_markup=await keyboard()
#
#     )


@user_main_panel.message(F.text == '/start')
async def start_command(message: Message):
    await message.delete()
    if await User.get(pk=message.from_user.id):
        await message.answer(text='Каталог товаров.', reply_markup=await keyboard())
    else:
        user = User(id=message.from_user.id, first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name)
        await user.save()
        await message.answer(text='Зарегистрирован.', reply_markup=await keyboard())


@user_main_panel.callback_query(UserCallbackData.filter((F.target == 'nok') & (F.action == 'get')))
async def user_main(callback: CallbackQuery):
    await callback.message.edit_text(
        text='выберите товар',
        reply_markup=await keyboard()
    )


@user_main_panel.message(F.text == 'ссылка')
async def my_ss_message(message: Message):
    await message.delete()
    await message.answer(text=f'ахуеный тг бот:'
                              f'https://xn--80affa3aj0al.xn--80asehdb/#@milvusdev10bot:', reply_markup=user_panel)


@user_main_panel.message(F.text == 'my_id')
async def my_id_massage(message: Message):
    await message.delete()
    await message.answer(text=f'Ваш персональный id: {message.from_user.id}', reply_markup=user_panel)


@user_main_panel.message(F.text == 'full_name')
async def full_name_message(message: Message):
    await message.delete()
    await message.answer(text=f'Ваше полное имя: {message.from_user.full_name}', reply_markup=user_panel)
    # await message.answer(text='полное имя', reply_markup=user_pan


@user_main_panel.message(F.text == 'item')
async def full_item_message(message: Message):
    await message.delete()
    if await User.get(pk=message.from_user.id):
        await message.answer(text='Каталог', reply_markup=await keyboard())
    else:
        user = User(id=message.from_user.id, first_name=message.from_user.first_name,
                    last_name=message.from_user.last_name)
        await user.save()
        await message.answer(text='Зарегистрирован.', reply_markup=await keyboard())


@user_main_panel.callback_query(UserCallbackData.filter((F.target == 'nok') & (F.action == 'all')))
async def user_main(callback: CallbackQuery):
    await callback.message.edit_text(
        text='выберите товар',
        reply_markup=await keyboard()
        # base
    )




