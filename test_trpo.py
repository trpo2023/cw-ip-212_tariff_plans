import pytest
from unittest.mock import patch, mock_open
import json
import io

from trpo import get_choice, choice_tariff, print_tariff_plans


@pytest.fixture
def tariff_plans():
    with open("tariff_plans.json") as file:
        data = json.load(file)

    tariff_plans = data["tariff_plans"]
    return tariff_plans

def test_get_choice_valid(monkeypatch):
    prompt = "Выберите количество минут разговора:"
    options = ["250 минут", "300 минут", "600 минут"]
    user_choice = "1"

    monkeypatch.setattr('builtins.input', lambda _: user_choice)

    choice = get_choice(prompt, options, user_choice)

    assert choice == "250 минут"


def test_get_choice_invalid_then_valid(monkeypatch):
    prompt = "Выберите количество минут разговора:"
    options = ["250 минут", "300 минут", "600 минут"]
    user_choices = ["4", "2"]

    monkeypatch.setattr('builtins.input', lambda _: user_choices.pop(0))

    choice = get_choice(prompt, options, user_choices[0])

    assert choice == "300 минут"


def test_choice_tariff_optimal_tariff_found(monkeypatch, tariff_plans):
    user_inputs = ["1", "1", "2", "3", "да", ""]
    expected_output = "Тариф успешно подключен!"

    monkeypatch.setattr('builtins.input', lambda _: user_inputs.pop(0) if user_inputs else "")

    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        choice_tariff(*user_inputs, tariff_plans=tariff_plans)

    assert expected_output in fake_output.getvalue()



def test_choice_tariff_optimal_tariff_not_found(monkeypatch, tariff_plans) -> None:
    user_inputs = ["1", "3", "2", "3", "нет", "нет", ""]
    expected_output = "Тариф не был подключен."

    monkeypatch.setattr('builtins.input', lambda _: user_inputs.pop(0))
    
    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        choice_tariff(*user_inputs, tariff_plans=tariff_plans)
    
    assert expected_output in fake_output.getvalue()


def test_print_tariff_plans():
    expected_output = "Тариф: MTS_access"
    
    with patch('builtins.open', mock_open(read_data=json.dumps(tariff_plans))):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print_tariff_plans(tariff_plans)