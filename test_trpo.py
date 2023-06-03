import pytest
from unittest.mock import patch
import json
import io

from main import get_choice, choice_tariff, print_tariff_plans


@pytest.fixture
def tariff_plans():
    return {
        "MTS_access": {
            "minutes": 5000,
            "messages": 1000,
            "internet": 50,
            "operator": "MTS",
            "monthly_cost": 790
        },
        "We_Are_MTS": {
            "minutes": 1200,
            "messages": 500,
            "internet": 45,
            "operator": "MTS",
            "monthly_cost": 850
        },
        # Другие тарифные планы
    }


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



def test_print_tariff_plans(tariff_plans):
    user_inputs = ["2", ""]
    expected_output = "Тариф: MTS_access"

    with patch('builtins.open', new=io.StringIO(json.dumps(tariff_plans))):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print_tariff_plans()

    assert expected_output in fake_output.getvalue()