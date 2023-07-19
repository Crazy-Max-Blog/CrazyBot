from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

from states import UserStates
from database import create_user, get_user
from keyboards.channels import commands_button
import data
print(data.a)

router = Router()

s = False


@router.message(lambda c: c.text in [f'/{key}' for key in data.comands])
async def start_command(message: Message, state: FSMContext):
    global s
    action = message.text.split('/')[1]
    await state.update_data(action=action)
    await state.set_state(UserStates.UPDATE_DATA)
    s = True
    await message.answer(data.comands[action]['m'])

@router.callback_query(lambda c: c.data in [f'{key}' for key in data.comands])
async def start_command(call: CallbackQuery, state: FSMContext):
    global s
    action = call.data
    await state.update_data(action=action)
    await state.set_state(UserStates.UPDATE_DATA)
    s = True
    await call.message.answer(data.comands[action]['m'])

@router.message(UserStates.UPDATE_DATA)
async def update_data(message: Message, state: FSMContext, bot: Bot):
    global s
    t = await state.get_data()
    value = message.text
    await message.answer('Ок, Спасибо')
    await message.answer('Команды бота:', reply_markup=commands_button())
    rm = InlineKeyboardBuilder()
    send_id = data.comands[t['action']]['send_id']
    if send_id:
        ac = t['action']
        rm.add(InlineKeyboardButton(text='Переслать в главный канал...', callback_data=f'sendchannel_{ac}'))
    await bot.send_message(chat_id = int(data.comands[t['action']]['id']), text=value, reply_markup=rm.as_markup())
    await state.clear()
    s = False

@router.callback_query(lambda c: c.data.startswith("sendchannel_"))
async def update_data(call: CallbackQuery, bot: Bot):
    t = call.data.split('_')[1]
    value = call.message.text
    await call.message.answer(text='Отправлено')
    await bot.send_message(chat_id = int(data.comands[t]['send_id']), text=value)

@router.message(lambda m: s==False)
async def commands_command(message: Message):
    await message.answer(data.m['error_c'])