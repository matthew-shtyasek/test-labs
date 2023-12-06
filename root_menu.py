from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common import make_reply_keyboard
from states import OrderLab


from lab1.common import main_menu as lab1_main_menu
from lab2.routing import main_menu as lab2_main_menu
from lab3.routing import main_menu as lab3_main_menu
from lab4.routing import main_menu as lab4_main_menu
from lab5.routing import main_menu as lab5_main_menu
from lab6.routing import main_menu as lab6_main_menu
from lab7.routing import main_menu as lab7_main_menu

router = Router()


@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    await begin_layout(message, state)


@router.message(
    OrderLab.choosing_lab_number,
    F.text.in_(OrderLab.available_names)
)
async def lab_choose(message: Message, state: FSMContext):
    lab_number = int(message.text[-1])
    await state.update_data(lab_number=lab_number)
    await message.answer(text='Вы выбрали лабораторную работу №' + str(lab_number))

    if lab_number == 1:
        await lab1_main_menu(message, state)
    elif lab_number == 2:
        await lab2_main_menu(message, state)
    elif lab_number == 3:
        await lab3_main_menu(message, state)
    elif lab_number == 4:
        await lab4_main_menu(message, state)
    elif lab_number == 5:
        await lab5_main_menu(message, state)
    elif lab_number == 6:
        await lab6_main_menu(message, state)
    elif lab_number == 7:
        await lab7_main_menu(message, state)


@router.message(OrderLab.choosing_lab_number)
async def incorrect_lab_choose(message: Message):
    await message.answer(
        text='Данная лабораторная работа ещё не выполнена',
        reply_markup=make_reply_keyboard(OrderLab.available_names)
    )


async def begin_layout(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите лабораторную работу",
        reply_markup=make_reply_keyboard(OrderLab.available_names, row_size=2)
    )
    await state.set_state(OrderLab.choosing_lab_number)


@router.message(F.text == 'В главное меню')
async def to_main_menu(message: Message, state: FSMContext):
    await begin_layout(message, state)
    