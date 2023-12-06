from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from common import make_reply_keyboard
from lab5.routing.main_menu import router as menu_router
from lab5.states import Actions

router = Router()
router.include_router(menu_router)


async def main_menu(message: Message, state: FSMContext):
    await message.answer(
        text='Теперь выберите что нужно сделать',
        reply_markup=make_reply_keyboard(list(Actions.available_actions.values()),
                                         row_size=2)
    )
    await state.set_state(Actions.lab5_main_menu)
