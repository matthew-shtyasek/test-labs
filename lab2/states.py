from aiogram.fsm.state import StatesGroup, State


class Actions(StatesGroup):
    available_actions = {'diagram1': 'Диаграмма v1',
                         'diagram2': 'Диаграмма v2',
                         'test1': 'Тест. v1',
                         'test2': 'Тест. v2',
                         'main_menu': 'В главное меню'}

    main_menu = State()
