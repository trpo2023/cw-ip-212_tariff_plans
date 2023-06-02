import io
import json
import unittest
import unittest.mock
import trpo

class TRPOTestCase(unittest.TestCase):
    def test_choice_tariff(self):
        user_input = "1\n1\n1\nДа\n"
        with unittest.mock.patch("builtins.input", side_effect=user_input.split()):
            trpo.choice_tariff.get_choice = trpo.get_choice  # Замена функции get_choice в choice_tariff.py
            trpo.choice_tariff()

        # Проверка значений переменных для оптимального тарифа
        self.assertEqual(trpo.choice_tariff.optimal_tariff_operator, "MTS")
        self.assertEqual(trpo.choice_tariff.tariff_optimal, "MTS_access")
        self.assertEqual(trpo.choice_tariff.minute_optimal, 5000)
        self.assertEqual(trpo.choice_tariff.message_optimal, 1000)
        self.assertEqual(trpo.choice_tariff.internet_optimal, 50)

    def test_print_tariff_plans(self):
        with open("tariff_plans.json") as file:
            data = json.load(file)
        expected_output = ""
        for tariff_plan in data["tariff_plans"]:
            plan = data["tariff_plans"][tariff_plan]
            expected_output += f"Тариф: {tariff_plan}\nОператор: {plan['operator']}\nМинуты: {plan['minutes']}\nСообщения: {plan['messages']}\nИнтернет: {plan['internet']} ГБ\n======================\n"
        
        with unittest.mock.patch("builtins.input", return_value=""):
            with unittest.mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
                trpo.print_tariff_plans()
                self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()