from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def start_menu_keyboard():
    buttons = [
        [KeyboardButton(text="Список ключей 📖"), KeyboardButton(text="Купить 🔑")],
        [KeyboardButton(text="Аккаунт 👤")]
        ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        one_time_keyboard=True,
        resize_keyboard=True
        )

def account_menu():
    buttons = [
        [KeyboardButton(text="Назад ⬅"), KeyboardButton(text="Пополнение 💸")]
    ]
    
    return ReplyKeyboardMarkup(
        keyboard=buttons,
        one_time_keyboard=True,
        resize_keyboard=True
        )

def topping_up_menu():
    buttons = [
        [KeyboardButton(text="300"), KeyboardButton(text="500"), KeyboardButton(text="700")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        one_time_keyboard=True,
        resize_keyboard=True
        )

def buy_menu():
    buttons = [
        [KeyboardButton(text="Vbucks"), KeyboardButton(text="Terraria"), KeyboardButton(text="RDR")],
        [KeyboardButton(text="Назад ⬅")]
    ]

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        one_time_keyboard=True,
        resize_keyboard=True
        )