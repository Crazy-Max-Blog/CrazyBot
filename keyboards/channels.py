from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

import data


def channels_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(len(data.m["channels"])):
        print(data.m["channels"][i][0], data.m["channels"][i][1])
        builder.add(InlineKeyboardButton(text=data.m["channels"][i][0], url=data.m["channels"][i][1]))
    '''builder.row(
        InlineKeyboardButton(text="👍1", callback_data=f"1like_{user_id}"),
        InlineKeyboardButton(text="👎1", callback_data=f"1dislike_{user_id}"),
        InlineKeyboardButton(text="⏹️1", callback_data=f"1stop"),
    )'''
    return builder.as_markup()

def commands_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    e = [['Вызов Принят', 'hub'], ['Идея для видео', 'idea'], ['Товар с Али', 'ali'], ['Новость', 'news'], ['Помощь', 'support']]
    for i in range(len(e)):
        print(e[i])
        builder.row(InlineKeyboardButton(text=e[i][0], callback_data=e[i][1]))
    '''builder.row(
        InlineKeyboardButton(text="👍1", callback_data=f"1like_{user_id}"),
        InlineKeyboardButton(text="👎1", callback_data=f"1dislike_{user_id}"),
        InlineKeyboardButton(text="⏹️1", callback_data=f"1stop"),
    )'''
    return builder.as_markup()