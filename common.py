from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types.base import MutableTelegramObject
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from pydantic import typing


def make_keyboard(type: str, items: list[str], row_size=3, **kwargs) -> MutableTelegramObject:
    if type == 'reply':
        Builder = ReplyKeyboardBuilder
        Button = KeyboardButton
    elif type == 'inline':
        Builder = InlineKeyboardBuilder
        Button = InlineKeyboardButton
    else:
        raise ValueError(f'Type "{type}" does not exists!')

    builder = Builder()

    if type == 'inline':
        buttons = [Button(text=item, callback_data=kwargs['callbacks'][i]) for i, item in enumerate(items)]
    else:
        buttons = [Button(text=item) for item in items]

    builder.add(*buttons)
    builder.adjust(row_size)
    return builder.as_markup(resize_keyboard=True)


def make_reply_keyboard(items: list[str], row_size=3) -> ReplyKeyboardMarkup:
    return typing.cast(ReplyKeyboardMarkup, make_keyboard('reply', items, row_size))


def make_inline_keyboard(items: list[str], callbacks: list[str], row_size=3) -> InlineKeyboardMarkup:
    return typing.cast(InlineKeyboardMarkup, make_keyboard('inline', items, row_size, callbacks=callbacks))
