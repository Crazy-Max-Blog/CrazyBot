from aiogram import Router, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

'''from keyboards.reg_kbs import name_kb, city_kb
from keyboards.menu_kb import menu_kb'''
from states import UserStates
from database import create_user, get_user
from keyboards.channels import channels_button
import data
print(data.a)

router = Router()


@router.message(lambda c: c.text in [f'/{key}' for key in data.comands])
async def start_command(message: Message, state: FSMContext):
    if message.text in [f'/{key}' for key in data.comands]:
        cmd, action = message.text.split('/')
        await state.update_data(action=action)
        await state.set_state(UserStates.UPDATE_DATA)
        await message.answer(data.comands[action]['m'])
        idd = data.comands

@router.callback_query(lambda c: c.data in [f'{key}' for key in data.comands])
async def start_command(call: CallbackQuery, state: FSMContext):
    action = call.data
    await state.update_data(action=action)
    await state.set_state(UserStates.UPDATE_DATA)
    await call.message.answer(data.comands[action]['m'])
    idd = data.comands

@router.message(UserStates.UPDATE_DATA)
async def update_data(message: Message, state: FSMContext, bot: Bot):
    t = await state.get_data()
    value = message.text
    await message.answer('Ок, Спасибо')
    rm = InlineKeyboardBuilder()
    send_id = data.comands[t['action']]['send_id']
    if send_id:
        ac = t['action']
        rm.add(InlineKeyboardButton(text='Переслать в главный канал...', callback_data=f'sendchannel_{ac}'))
    await bot.send_message(chat_id = int(data.comands[t['action']]['id']), text=value, reply_markup=rm.as_markup())
    await state.clear()

@router.callback_query(lambda c: c.data.startswith("sendchannel_"))
async def update_data(call: CallbackQuery, state: FSMContext, bot: Bot):
    cmd, t = call.data.split('_')
    value = call.message.text
    send_id = int(data.comands[t]['send_id'])
    await call.message.answer(text=f'{send_id} {value}')
    await bot.send_message(chat_id = int(data.comands[t]['send_id']), text=value)