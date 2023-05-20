import unittest
from unittest.mock import patch
from io import StringIO

import json

with open('tariff_plans.json', 'r') as f:
    tariff_plans = json.load(f)
    
class TestTRPO(unittest.TestCase):
    def test_calculate_total_cost(self):
        # Тестирование функции calculate_total_cost

        # Тестовые данные
        minutes = 250
        messages = 100
        data_usage = 5

        # Ожидаемый результат
        expected_result = 600

        # Вызов функции
        result = trpo.calculate_total_cost(minutes, messages, data_usage)

        # Проверка результата
        self.assertEqual(result, expected_result)

    @patch('builtins.input', side_effect=["1"])
    def test_get_minutes(self, mock_input):
        # Тестирование функции get_minutes

        # Ожидаемый вывод
        expected_output = "Выберите количество минут разговора:\n1. 250 минут\n2. 300 минут\n3. 600 минут\n4. 1200 минут\n5. 3000 минут\n6. 5000 минут\n"

        # Захват вывода
        captured_output = StringIO()

        # Запуск функции с захватом вывода
        with patch('sys.stdout', new=captured_output):
            trpo.get_minutes()

        # Проверка вывода
        self.assertEqual(captured_output.getvalue(), expected_output)
        # Проверка значения переменной minutes
        self.assertEqual(trpo.minutes, 250)

if __name__ == '__main__':
    unittest.main()