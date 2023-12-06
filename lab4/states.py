from aiogram.fsm.state import StatesGroup, State


class Actions(StatesGroup):
    available_actions = {'diagram': 'Дерево решений',
                         'test1': 'Тест v1',
                         'test2': 'Тест v2',
                         'main_menu': 'В главное меню'}

    lab4_main_menu = State()
