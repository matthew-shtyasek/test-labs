from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common import make_reply_keyboard
from lab1.states import Diagram


preferences = {
    'default': {
        'legend': True,
        'palette': '',
        'size': (16, 9),
    }
}


async def main_menu(message: Message, state: FSMContext):
    await message.answer(
        text='Теперь выберите что нужно сделать',
        reply_markup=make_reply_keyboard(Diagram.available_actions)
    )
    await state.set_state(Diagram.choosing_actions)