from aiogram import types, F, Router
from aiogram.filters.command import Command
import logging
import random
from keyboards.keyboards import kb1, kb2
from utils.random_fox import fox


router = Router()


#Хэндлер на команду /start
@router.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}', reply_markup=kb1)


#Хэндлер на команду /stop
@router.message(Command('stop'))
async def cmd_stop(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Пока, {name}')


#Хэндлер на команду /fox
@router.message(Command('fox'))
@router.message(Command('лиса'))
@router.message(F.text.lower() == 'покажи лису')
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.answer(f'Держи лису, {name}')
    await message.answer_photo(photo=img_fox)
# await message.answer_
# await bot.send_photo(message.from_user.id, photo=img_fox)
    
#Хэндлер на команду /cat
@dp.message(Command('cat'))
@dp.message(Command('кот'))
@dp.message(Command('кота'))
@dp.message(Command('котов'))
@dp.message(Command('кошка'))
@dp.message(Command('кошку'))
@dp.message(Command('кошек'))
@dp.message(Command('котенок'))
@dp.message(Command('котенка'))
@dp.message(Command('котят'))
@dp.message(F.text.lower() == 'покажи кота')
async def cmd_cat(message: types.Message):
    name = message.chat.first_name
    img_cat = cat()
    await message.answer(f'Держи котов, {name}')
    await message.answer_photo(photo=img_cat)
# await bot.send_photo(message.from_user.id, photo=img_cat)



#Хендлер на сообщения
@router.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer_dice(emoji="🎲")
    elif 'лиса' in msg_user:
        await message.answer(f'Смотри что у меня есть, {name}', reply_markup=kb2)
    else:
        await message.answer(f'Я не знаю такого слова')