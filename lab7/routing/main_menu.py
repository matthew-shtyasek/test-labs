import asyncio

from typing import Optional

from aiogram import Router, F
from aiogram.fsm.state import State
from aiogram.types import Message, FSInputFile

from lab7.states import Actions
from lab7.tests import GraphTests

router = Router()


@router.message(Actions.lab7_main_menu,
                F.text.in_([Actions.available_actions['test1']]))
async def send_tests(message: Message, state: State):
    def output_format(data):
        result: str = ''

        for item in data:
            function, xs, y_real, y = item
            if isinstance(y_real, float):
                y_real = round(y_real, 4)
            if isinstance(y, float):
                y = round(y, 4)
            xs, y_real, y = str(xs), str(y_real), str(y)
            result += f'Для истинного {function} = {y_real} получен f(x) = {y} при:\n'
            result += f'{xs}\n'
        return result

    test = GraphTests()

    client_test_result, functions_test_result = test.integration_test()

    await message.answer('Тесты функций нижнего уровня:')
    await asyncio.sleep(0.3)
    await message.answer(
        f'Неуспешно:\n{(output_format(functions_test_result["correct"]) if functions_test_result["correct"] else "Нет")}')
    await asyncio.sleep(0.3)
    await message.answer(
        f'Успешно:\n{(output_format(functions_test_result["errors"]) if functions_test_result["errors"] else "Нет")}')

    await asyncio.sleep(0.3)

    await message.answer('Тесты функции верхнего уровня:')
    await asyncio.sleep(0.3)
    await message.answer(
        f'Неуспешно:\n{(output_format(client_test_result["correct"]) if client_test_result["correct"] else "Нет")}')
    await asyncio.sleep(0.3)
    await message.answer(
        f'Успешно:\n{(output_format(client_test_result["errors"]) if client_test_result["errors"] else "Нет")}')


