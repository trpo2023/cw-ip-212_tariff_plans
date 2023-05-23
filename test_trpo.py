import unittest
from io import StringIO
import sys
import json
from unittest.mock import patch
from trpo import main_menu, choice_tariff, print_tariff_plans


class TariffProgramTests(unittest.TestCase):
    def setUp(self):
        self.data = {
            "tariff_plans": {
                "Тариф 1": {
                    "minutes": 250,
                    "messages": 200,
                    "internet": 1,
                    "operator": "Оператор 1"
                },
                "Тариф 2": {
                    "minutes": 300,
                    "messages": 300,
                    "internet": 3,
                    "operator": "Оператор 2"
                },
                "Тариф 3": {
                    "minutes": 600,
                    "messages": 400,
                    "internet": 5,
                    "operator": "Оператор 3"
                }
            }
        }

    def test_choice_tariff_valid_input(self):
        with patch('builtins.input', side_effect=['1', '1', '1', 'да']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                with open("tariff_plans.json", "w") as file:
                    json.dump(self.data, file)
                choice_tariff()
                expected_output = '''\
======================
Рекомендуемый тариф:
Тариф: Тариф 1
Оператор: Оператор 1
Минуты: 250
Сообщения: 200
Интернет: 1 ГБ
======================
Вы хотите подключить данный тариф? (Да/Нет): 
Тариф успешно подключен!
'''
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_choice_tariff_invalid_input(self):
        with patch('builtins.input', side_effect=['7', '10', '11', 'нет']):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                with open("tariff_plans.json", "w") as file:
                    json.dump(self.data, file)
                choice_tariff()
                expected_output = '''\
Выберите количество минут разговора:
Некорректный выбор. Введите номер выбранного варианта: 
Некорректный выбор. Введите номер выбранного варианта: 
Выберите количество интернет-трафика:
Некорректный выбор. Введите номер выбранного варианта: 
К сожалению, не удалось найти подходящий тариф.
'''
                self.assertEqual(fake_output.getvalue(), expected_output)

    def test_print_tariff_plans(self):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with open("tariff_plans.json", "w") as file:
                json.dump(self.data, file)
            print_tariff_plans()
            expected_output = '''\
Доступные тарифы:
======================
Тариф: Тариф 1
Минуты: 250
Сообщения: 200
Интернет: 1 ГБ
Оператор: Оператор 1



