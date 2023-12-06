from aiogram.fsm.state import StatesGroup, State


class Actions(StatesGroup):
    available_actions = {'test1': 'Тестировать',
                         'main_menu': 'В главное меню'}

    lab7_main_menu = State()
