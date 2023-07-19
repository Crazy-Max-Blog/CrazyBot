from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

'''from keyboards.reg_kbs import name_kb, city_kb
from keyboards.menu_kb import menu_kb'''
from states import UserStates
from database import create_user, get_user
from keyboards import channels
import data
print(data.a)

router = Router()


@router.message(Command("start"))
async def start_command(message: Message, state: FSMContext):
    user = get_user(message.from_user.id)
    print(user)
    if user:
        await state.clear()
        return await message.answer(data.m['cancel'])
    await message.answer(data.m['help'], reply_markup=channels.channels_button())
    await message.answer('Команды бота:', reply_markup=channels.commands_button())
    create_user(message.from_user.id, message.from_user.first_name, data="")

@router.message(Command("help"))
async def help_command(message: Message):
    await message.answer(data.m['help'], reply_markup=channels.channels_button())
    await message.answer('Команды бота:', reply_markup=channels.commands_button())

@router.message(Command("commands"))
async def commands_command(message: Message):
    await message.answer('Команды бота:', reply_markup=channels.commands_button())