from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from gen import UserCallbackData


async def keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text='нажмите',
                callback_data=UserCallbackData(
                    target='nok',
                    action='get',
                    ram='c'
                ).pack()
            )
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)



# user_data = {}
#
#
# async def get_keyboard() -> InlineKeyboardMarkup:
#     buttons = [
#         [
#             InlineKeyboardButton(text="-1", callback_data="num_decr"),
#             InlineKeyboardButton(text="+1", callback_data="num_incr")
#         ],
#         [InlineKeyboardButton(text="Подтвердить", callback_data="num_finish")]
#     ]
#     keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
#     return keyboard
#
#
# async def update_num_text(message: types.Message, new_value: int):
#     await message.edit_text(
#         f"Укажите число: {new_value}",
#         reply_markup=get_keyboard()
#     )
