import unittest
from unittest.mock import patch

import main


class TestMain(unittest.TestCase):
    @patch("main.get_minutes", return_value=100)
    @patch("main.choose_messages", return_value=50)
    @patch("main.choose_data_usage", return_value=10)
    @patch("builtins.input", side_effect=["1", "n"])
    def test_main(self, input_mock, data_usage_mock, messages_mock, minutes_mock):
        main.main()
        expected_output = "Рекомендуем вам тарифный план: smart\nКолличество сообщений: 100\nКолличество минут: 500\nКолличество интернета в ГБ: 20\n"
        self.assertEqual(expected_output, main_output.getvalue())

    @patch("builtins.input", side_effect=["100", "n"])
    def test_get_minutes(self, input_mock):
        self.assertEqual(100, main.get_minutes())

    @patch("builtins.input", side_effect=["50", "n"])
    def test_choose_messages(self, input_mock):
        self.assertEqual(50, main.choose_messages())

    @patch("builtins.input", side_effect=["10", "n"])
    def test_choose_data_usage(self, input_mock):
        self.assertEqual(10, main.choose_data_usage())


if __name__ == "__main__":
    unittest.main()
