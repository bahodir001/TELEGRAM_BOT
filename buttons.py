from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Pictures"),
            KeyboardButton(text="Add picture")
        ]
    ], resize_keyboard=True
)