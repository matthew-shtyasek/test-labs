from typing import Optional

from aiogram import Router, F
from aiogram.fsm.state import State
from aiogram.types import Message, FSInputFile

from lab4.program import correct_algorithm, incorrect_algorithm
from lab4.states import Actions
from lab4.tests import GraphTests

router = Router()


@router.message(Actions.lab4_main_menu,
                F.text.in_([Actions.available_actions['diagram']]))
async def send_diagram(message: Message, state: State):
    file_name = 'lab4/media/'
    answer: Optional[str]

    file_name += 'diagram.png'
    answer = 'Дерево решений'

    print(file_name)
    photo = FSInputFile(file_name)
    await message.answer_photo(photo, answer)


@router.message(Actions.lab4_main_menu,
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

    test: Optional[GraphTests]

    if message.text == Actions.available_actions['test1']:
        test = GraphTests(func=correct_algorithm)
        await message.answer('При корректном алгоритме:')
    else:
        test = GraphTests(func=incorrect_algorithm)
        await message.answer('При некорректном алгоритме:')

    first_branch_result = test.algorithm_test()

    await message.answer('Тесты :')
    await message.answer(f'Неуспешно:\n{(output_format(first_branch_result["correct"]) if first_branch_result["correct"] else "Нет")}')
    await message.answer(f'Успешно:\n{(output_format(first_branch_result["errors"]) if first_branch_result["errors"] else "Нет")}')
