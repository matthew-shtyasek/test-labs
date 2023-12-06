from aiogram.fsm.state import StatesGroup, State


class Diagram(StatesGroup):
    ACTION_SHOW = 0
    ACTION_SETTINGS = 1
    ACTION_CHOOSE_TESTS = 2
    ACTION_TO_MENU = 3

    available_actions = ['Показать диаграмму',
                         'Настройки диаграммы',
                         'Выбор группы тестов',
                         'В главное меню']

    choosing_actions = State()
    show_diagram = State()
    show_settings = State()
    change_diagram = State()
    choosing_test_groups = State()


class DiagramSettings(StatesGroup):
    ACTION_SHOW_LEGEND = 0
    ACTION_CHANGE_PALETTE = 1
    ACTION_CHANGE_SIZE = 2
    ACTION_RESTORE_DEFAULTS = 3
    ACTION_BACK = 4

    available_setting = ['Отображение легенды',
                         'Палитра цветов',
                         'Размер диаграммы',
                         'Сброс настроек',
                         'Назад']

    choosing_legend = State()
    choosing_color_palette = State()
    choosing_size = State()
    settings_mode = State()
