"""Набор модульных тестов pytest для лабораторной работы №2 (Вариант 6)."""

import os
import pytest
from src.number_series import sum_odd_numbers
from src.calculator import calculate
from src.strings_ops import reverse_string
from src.plotting import plot_parabola
from src.serializer import serialize_data, deserialize_data


class TestSumOddNumbers:
    def test_positive_odd_bound(self):
        assert sum_odd_numbers(5) == 1 + 3 + 5  # 9

    def test_positive_even_bound(self):
        assert sum_odd_numbers(6) == 1 + 3 + 5  # 9

    def test_single_element(self):
        assert sum_odd_numbers(1) == 1

    def test_zero_and_negative(self):
        assert sum_odd_numbers(0) == 0
        assert sum_odd_numbers(-10) == 0

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            sum_odd_numbers("10")  # type: ignore


class TestCalculator:
    def test_basic_arithmetic(self):
        assert calculate(10, 5, "+") == 15.0
        assert calculate(10, 5, "-") == 5.0
        assert calculate(10, 5, "*") == 50.0
        assert calculate(10, 5, "/") == 2.0

    def test_additional_operators(self):
        assert calculate(2, 3, "**") == 8.0
        assert calculate(10, 3, "//") == 3.0
        assert calculate(10, 3, "%") == 1.0

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            calculate(10, 0, "/")
        with pytest.raises(ZeroDivisionError):
            calculate(10, 0, "//")
        with pytest.raises(ZeroDivisionError):
            calculate(10, 0, "%")

    def test_invalid_operator(self):
        with pytest.raises(ValueError):
            calculate(10, 5, "^")


class TestReverseString:
    def test_simple_reverse(self):
        assert reverse_string("Python") == "nohtyP"

    def test_empty_string(self):
        assert reverse_string("") == ""

    def test_palindrome(self):
        assert reverse_string("radar") == "radar"

    def test_unicode_and_spaces(self):
        assert reverse_string("Привет, Мир!") == "!риМ ,тевирП"


class TestPlotting:
    def test_plot_generation(self, tmp_path):
        target = tmp_path / "test_parabola.png"
        path = plot_parabola(x_min=-5.0, x_max=5.0, points=50, output_path=str(target))
        assert os.path.exists(path)
        assert os.path.getsize(path) > 1000

    def test_invalid_bounds(self):
        with pytest.raises(ValueError):
            plot_parabola(x_min=10.0, x_max=5.0)


class TestJsonSerialization:
    def test_roundtrip_dict(self, tmp_path):
        test_file = tmp_path / "test.json"
        data = {"title": "Lab2", "variant": 6, "passed": True, "items": [1, 2, 3]}
        raw_json = serialize_data(data, filepath=str(test_file))
        assert "Lab2" in raw_json
        loaded = deserialize_data(filepath=str(test_file))
        assert loaded == data

    def test_deserialize_from_string(self):
        json_str = '{"status": "ok", "value": 42}'
        data = deserialize_data(json_str=json_str)
        assert data["status"] == "ok"
        assert data["value"] == 42
