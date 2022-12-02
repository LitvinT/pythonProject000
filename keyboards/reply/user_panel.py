from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

user_panel = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=False,
    request_contact=True,
    request_location=True,
    keyboard=[
        [
            KeyboardButton(
                text='/start'
            ),
            KeyboardButton(
                text='ссылка'
            ),
            KeyboardButton(
                text='full_name'
            ),
            KeyboardButton(
                text='item'
            ),
            KeyboardButton(
                text='my_id'
            )
        ]
    ]
)


