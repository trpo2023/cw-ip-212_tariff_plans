import pytest
from unittest.mock import patch
import json
import unittest
import unittest.mock
import trpo

    with patch('sys.stdout', new=io.StringIO()) as fake_output:
        choice_tariff(*user_inputs, tariff_plans=tariff_plans)

    assert expected_output in fake_output.getvalue()


def test_print_tariff_plans(tariff_plans):
    expected_output = "Тариф: MTS_access"

    with patch('builtins.open', new=io.StringIO(json.dumps(tariff_plans))):
        with patch('sys.stdout', new=io.StringIO()) as fake_output:
            print_tariff_plans()

    assert expected_output in fake_output.getvalue()