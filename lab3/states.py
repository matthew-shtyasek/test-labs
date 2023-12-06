from aiogram.fsm.state import StatesGroup, State


class Actions(StatesGroup):
    available_actions = {'diagram': 'Потоковый граф',
                         'test1': 'Тест. b1',
                         'test2': 'Тест. b2',
                         'main_menu': 'В главное меню'}

    main_menu = State()
