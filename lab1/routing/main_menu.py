import os

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from common import make_reply_keyboard
from lab1.common import preferences
from lab1.states import Diagram, DiagramSettings
from lab1.test_logic import load_df, draw_graphic

router = Router()


def get_user_preferences(user_id):
    if user_id not in preferences:
        return preferences['default']
    return preferences[user_id]


@router.message(
    Diagram.choosing_actions,
    F.text == Diagram.available_actions[Diagram.ACTION_CHOOSE_TESTS]
)
async def choose_tests(message: Message, state: FSMContext):
    await message.answer('Введите номер группы тестов:')
    await state.set_state(Diagram.choosing_test_groups)


@router.message(
    Diagram.choosing_test_groups,
    F.text.regexp('^[0-9]{1,}$')
)
async def set_test_group(message: Message, state: FSMContext):
    lpref = get_user_preferences(message.from_user.id)
    data = load_df(int(message.text))

    await state.set_state(Diagram.choosing_actions)
    if not data[0]:
        await message.answer(f'Группы тестов #{message.text} не существует!')
        await message.answer(f'Возвращаюсь в главное меню лабораторной работы №1')
        return

    path_to_img = draw_graphic(data, **lpref)
    photo = FSInputFile(path_to_img)
    await message.answer_photo(photo, 'Ваша диаграмма готова!')
    os.remove(path_to_img)


@router.message(
    Diagram.choosing_test_groups
)
async def incorrect_set_test_group(message: Message, state: FSMContext):
    await message.answer(f'Некорректная группа тестов "{message.text}".\nГруппой тестов может являться только целое число!')
    await message.answer('Возвращаюсь в главное меню лабораторной работы №1')
    await state.set_state(Diagram.choosing_actions)


@router.message(
    Diagram.choosing_actions,
    F.text == Diagram.available_actions[Diagram.ACTION_SHOW]
)
async def show_diagram(message: Message, state: FSMContext):
    lpref = get_user_preferences(message.from_user.id)

    data = load_df()
    path_to_img = draw_graphic(data, **lpref)
    photo = FSInputFile(path_to_img)
    await message.answer_photo(photo, 'Ваша диаграмма готова!')
    os.remove(path_to_img)


@router.message(
    Diagram.choosing_actions,
    F.text == Diagram.available_actions[Diagram.ACTION_SETTINGS]
)
async def settings_menu(message: Message, state: FSMContext):
    await state.set_state(Diagram.show_settings)
    await setting_up_diagram(message, state)


async def setting_up_diagram(message: Message, state: FSMContext):
    await message.answer('Вы перешли в меню выбора настроек',
                         reply_markup=make_reply_keyboard(DiagramSettings.available_setting))
    await state.set_state(DiagramSettings.settings_mode)
