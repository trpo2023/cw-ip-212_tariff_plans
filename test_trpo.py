import trpo
import unittest
from unittest.mock import patch
import io
import json
import sys
from trpo import main_menu, choice_tariff, print_tariff_plans

class TariffMenuTestCase(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        with open("tariff_plans.json") as file:
            self.data = json.load(file)

    @patch("builtins.input")
    def test_main_menu(self, mock_input):
        mock_input.side_effect = ["1", "2", "1", "4", "3"]  # Симулируем ввод пользователя
        expected_output = (
            "Выберите оператора:\n"
            "1. MTS\n"
            "2. Beeline\n"
            "3. TELE2\n"
            "4. Megafon\n"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            main_menu()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch("builtins.input")
    def test_choice_tariff(self, mock_input):
        mock_input.side_effect = ["1", "2", "3", "4"]  # Симулируем ввод пользователя
        expected_output = (
            "======================\n"
            "Рекомендуемый тариф:\n"
            "Тариф: The_tariff_is_higher\n"
            "Оператор: MTS\n"
            "Минуты: 600\n"
            "Сообщения: 600\n"
            "Интернет: 35 ГБ\n"
            "======================\n"
            "Вы хотите подключить данный тариф? (Да/Нет): \n"
            "Тариф успешно подключен!"
        )
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            choice_tariff()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_print_tariff_plans(self, mock_stdout):
        expected_output = (
            "Доступные тарифы:\n"
            "======================\n"
            "Тариф: MTS_access\n"
            "Минуты: 5000\n"
            "Сообщения: 1000\n"
            "Интернет: 50 ГБ\n"
            "Оператор: MTS\n"
            "======================\n"
            
        )
        print_tariff_plans()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

if __name__ == "__trpo__":
    unittest.trpo()
