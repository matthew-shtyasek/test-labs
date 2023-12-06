from typing import Optional

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State
from aiogram.types import Message, FSInputFile

from lab2.program import correct_algorithm, incorrect_algorithm
from lab2.states import Actions
from lab2.tests import WhiteBoxTests

router = Router()


@router.message(Actions.main_menu,
                F.text.in_([Actions.available_actions['diagram1'],
                            Actions.available_actions['diagram2']]))
async def send_diagram(message: Message, state: State):
    file_name = 'lab2/media/'
    answer: Optional[str]

    if message.text == Actions.available_actions['diagram1']:
        file_name += 'diagram_correct.png'
        answer = 'Блок-схема корректного алгоритма'
    else:
        file_name += 'diagram_incorrect.png'
        answer = 'Блок-схема алгоритма с ошибкой'

    photo = FSInputFile(file_name)
    await message.answer_photo(photo, answer)


@router.message(Actions.main_menu,
                F.text.in_([Actions.available_actions['test1'],
                            Actions.available_actions['test2']]))
async def send_tests(message: Message, state: State):
    def output_format(data):
        result: str = ''

        for item in data:
            xs, y_real, y = item
            result += f'Для истинного f(x) = {y_real:.4f} получен f(x) = {y:.4f} при:\n'
            for key, value in xs.items():
                result += f'{key} = {value}\n'
            result += '\n'
        return result[:-1]

    test: Optional[WhiteBoxTests]

    if message.text == Actions.available_actions['test1']:
        test = WhiteBoxTests(func=correct_algorithm)
        await message.answer('При корректном алгоритме:')
    else:
        test = WhiteBoxTests(func=incorrect_algorithm)
        await message.answer('При некорректном алгоритме:')

    c0_result = test.c0_tests()
    c1_result = test.c1_tests()
    c2_result = test.c2_tests()

    await message.answer('Для тестов C0:')
    await message.answer(f'Неуспешно:\n{(output_format(c0_result["correct"]) if c0_result["correct"] else "Нет")}')
    await message.answer(f'Успешно:\n{(output_format(c0_result["errors"]) if c0_result["errors"] else "Нет")}')

    await message.answer('Для тестов C1:')
    await message.answer(f'Неуспешно:\n{(output_format(c1_result["correct"]) if c1_result["correct"] else "Нет")}')
    await message.answer(f'Успешно:\n{(output_format(c1_result["errors"]) if c1_result["errors"] else "Нет")}')

    await message.answer('Для тестов C2:')
    await message.answer(f'Неуспешно:\n{(output_format(c2_result["correct"]) if c2_result["correct"] else "Нет")}')
    await message.answer(f'Успешно:\n{(output_format(c2_result["errors"]) if c2_result["errors"] else "Нет")}')

