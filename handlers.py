from aiogram import Router, F
from aiogram.types import Message

from keyboards import start_menu_keyboard, account_menu, topping_up_menu, buy_menu
from utils import get_products

products = [
    {"id": 1, "name": "Vbucks", "key": "1111-1111-1111", "price": 500},
    {"id": 2, "name": "Terraria", "key": "2222-2222-2222", "price": 300},
    {"id": 3, "name": "RDR", "key": "3333-3333-3333", "price": 200},
]

account = {"balance": 0}

router = Router()

@router.message(F.text.in_(["Назад ⬅", "/start"]))
async def start(message: Message):
    answer_text = f"Привет {message.from_user.first_name}.\n" \
            "Ты попал в магазин ключей <b>KeysStore</b> 🔑"
    await message.answer(text=answer_text, reply_markup=start_menu_keyboard())


@router.message(F.text == "Список ключей 📖")
async def values_list(message: Message):
    answer_text = get_products(products)

    await message.answer(text=answer_text, reply_markup=start_menu_keyboard())


@router.message(F.text == "Аккаунт 👤")
async def account_hanler(message: Message):
    answer_text = f"Имя аккаунта: {message.from_user.first_name}\n" \
                  f"Баланс аккаунта: {account.get("balance")}руб." \
                  
    await message.answer(text=answer_text, reply_markup=account_menu())


@router.message(F.text == "Купить 🔑")
async def product_selection(message: Message):
    answer_text = f"Ваш баланс: {account.get("balance")}\n\n" + get_products(products)
    await message.answer(answer_text)
    await message.answer(text="Выберите нужный продукт", reply_markup=buy_menu())


@router.message(F.text.in_([product.get("name") for product in products]))
async def buy_key_handler(message: Message):
    answer_text = f"Привет {message.from_user.first_name}.\n" \
                   "Ты попал в магазин ключей <b>KeysStore</b> 🔑"
    data = message.text
    price = 0
    for product in products:
        if product.get("name") == data:
            price = product.get("price")
            break
    
    if not price:
        await message.answer(text="Такой позиции нет!")
        return
    
    balance = account.get("balance")

    if balance < price:
        await message.answer(text="У вас не хватает денег!", reply_markup=buy_menu())
        await message.answer(text=answer_text, reply_markup=start_menu_keyboard())
        return
    
    balance -= price
    account.update({"balance": balance})
    await message.answer(f"Покупка прошла успешна!\nВаш ключ: {product.get("key")}")
    await message.answer(text=answer_text, reply_markup=start_menu_keyboard())


@router.message(F.text == "Пополнение 💸")
async def topping_up_balance_start(message: Message):
    await message.answer("Выбирети нужную сумму", reply_markup=topping_up_menu())


@router.message(F.text.in_(["300", "500", "700"]))
async def topping_up_balance_finish(message: Message):
    balance = account.get("balance")
    data = message.text
    answer_text = f"Имя аккаунта: {message.from_user.first_name}\n"
                               
    if data.isdigit():
        balance += int(data)
        account.update({"balance": balance})
        await message.answer("Пополнено успешно!")
        answer_text += f"Баланс аккаунта: {balance}руб."
        await message.answer(answer_text, reply_markup=account_menu())
        return

    answer_text += f"Баланс аккаунта: {balance}руб."
    await message.answer("Повторите попытку позже!", reply_markup=account_menu())
    await message.answer(answer_text, reply_markup=account_menu())