from aiogram.fsm.state import StatesGroup, State


class OrderLab(StatesGroup):
    available_names = ['Лабораторная работа №1',
                       'Лабораторная работа №2',
                       'Лабораторная работа №3',
                       'Лабораторная работа №4',
                       'Лабораторная работа №5',
                       'Лабораторная работа №6',
                       'Лабораторная работа №7',
                       'Лабораторная работа №8']
    choosing_lab_number = State()
