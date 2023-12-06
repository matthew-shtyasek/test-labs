import copy

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from common import make_inline_keyboard
from lab1.common import preferences, main_menu
from lab1.states import DiagramSettings
from lab1.test_logic import available_palettes


MAX_SIZE = 4_000


router = Router()


def get_user_preferences(user_id: int):
    if user_id in preferences:
        return preferences[user_id]
    preferences[user_id] = copy.copy(preferences['default'])
    return preferences[user_id]


'''=============================================RESTORE DEFAULTS======================================================='''


@router.message(
    DiagramSettings.settings_mode,
    F.text == DiagramSettings.available_setting[DiagramSettings.ACTION_RESTORE_DEFAULTS]
)
async def restore2defaults(message: Message, state: FSMContext):
    user_preferences = get_user_preferences(message.from_user.id)
    for key, value in preferences['default'].items():
        user_preferences[key] = value

    await message.answer('Настройки сброшены!')


'''=============================================SIZES======================================================='''


@router.message(
    DiagramSettings.settings_mode,
    F.text == DiagramSettings.available_setting[DiagramSettings.ACTION_CHANGE_SIZE]
)
async def choosing_size(message: Message, state: FSMContext):
    await message.answer('Введите размер диаграммы.\nРазмер вводится в формате "w h" (без кавычек), где w - ширина, h - высота.')
    await state.set_state(DiagramSettings.choosing_size)


@router.message(
    DiagramSettings.choosing_size,
    F.text.regexp(r'^[0-9]{1,}\s[0-9]{1,}$')
)
async def set_size(message: Message, state: FSMContext):
    w, h = message.text.split()
    w, h = int(w), int(h)
    if w * 100 > MAX_SIZE or h * 100 > MAX_SIZE:
        await message.answer(f'Размер {w, h} слишком большой.\nРазмер диаграммы не должен превышать {int(MAX_SIZE / 100)}!')
        await message.answer('Попробуйте ещё раз!')
        return

    user_preferences = get_user_preferences(message.from_user.id)
    user_preferences['size'] = (w, h)

    await message.answer(f'Размер диаграммы изменён на {w, h}')
    await state.set_state(DiagramSettings.settings_mode)


@router.message(
    DiagramSettings.choosing_size
)
async def incorrect_set_size(message: Message, state: FSMContext):
    await message.answer(f'"{message.text}" не является размером!\nПерехожу в режим выбора настроек.')
    await state.set_state(DiagramSettings.settings_mode)


'''=============================================PALETTES======================================================='''


@router.message(
    DiagramSettings.settings_mode,
    F.text == DiagramSettings.available_setting[DiagramSettings.ACTION_CHANGE_PALETTE]
)
async def choose_palette(message: Message, state: FSMContext):
    await message.answer('Доступны следующие палитры:',
                         reply_markup=make_inline_keyboard(list(available_palettes.keys()),
                                                           callbacks=[f'lab1_change_palette_{palette.lower()}'
                                                                      for palette in list(available_palettes.keys())],
                                                           row_size=int(len(list(available_palettes)) / 2)))


@router.callback_query(
    F.data.startswith('lab1_change_palette_')
)
async def change_palette(callback: CallbackQuery, state: FSMContext):
    palette = callback.data.split('palette_')[1].upper()

    user_preferences = get_user_preferences(callback.from_user.id)
    user_preferences['palette'] = palette

    await callback.message.reply(f'Установлена палитра "{palette}"')


'''=============================================LEGEND======================================================='''


@router.message(
    DiagramSettings.settings_mode,
    F.text == DiagramSettings.available_setting[DiagramSettings.ACTION_SHOW_LEGEND]
)
async def change_legend_visible(message: Message, state: FSMContext):
    await message.answer('Вы хотите, чтобы легенда отображалась на диаграмме?',
                         reply_markup=make_inline_keyboard(['Да', 'Нет'], callbacks=['lab1_legend_settings_yes', 'lab1_legend_settings_no']))


@router.callback_query(
    F.data.startswith('lab1_legend_settings_')
)
async def choosing_legend_visible(callback: CallbackQuery):
    legend = True if callback.data.endswith('yes') else False

    user_preferences = get_user_preferences(callback.from_user.id)
    user_preferences['legend'] = legend

    await callback.message.reply(f'Настройки успешно изменены:\nТеперь легенда {("отображается" if legend else "не отображается")}')


'''=============================================BACK======================================================='''


@router.message(
    DiagramSettings.settings_mode,
    F.text == DiagramSettings.available_setting[DiagramSettings.ACTION_BACK]
)
async def back_from_settings(message: Message, state: FSMContext):
    await main_menu(message, state)




