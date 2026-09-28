"""Главный модуль демонстрации решений лабораторной работы №2 (Вариант 6)."""

import os
from src.number_series import sum_odd_numbers
from src.calculator import calculate
from src.strings_ops import reverse_string
from src.plotting import plot_parabola
from src.serializer import serialize_data, deserialize_data


def main() -> None:
    print("=" * 60)
    print("Лабораторная работа №2 — Вариант 6")
    print("Дисциплина: «Методы и технологии программирования»")
    print("Студент: Вафин Денис Наильевич (Группа 221141)")
    print("=" * 60)

    # 1. Задание 2 (среднее): Сумма нечётных чисел до N
    n = 15
    odd_sum = sum_odd_numbers(n)
    print(f"\n[1] Сумма нечётных чисел до {n}: {odd_sum}")
    print(f"    Ряд: {[i for i in range(1, n + 1, 2)]}")

    # 2. Задание 6 (среднее): Калькулятор
    a, b = 25.0, 4.0
    print(f"\n[2] Калькулятор ({a} и {b}):")
    for op in ["+", "-", "*", "/", "**", "//", "%"]:
        res = calculate(a, b, op)
        print(f"    {a} {op} {b} = {res}")

    # 3. Задание 8 (среднее): Перевернуть строку
    original = "Методы и технологии программирования 2026"
    reversed_text = reverse_string(original)
    print("\n[3] Переворот строки:")
    print(f"    Исходная:   '{original}'")
    print(f"    Результат:  '{reversed_text}'")

    # 4. Задание 4 (повышенное): Построение графика y=x^2
    plot_file = "parabola.png"
    saved_path = plot_parabola(
        x_min=-10.0, x_max=10.0, points=300, output_path=plot_file
    )
    print("\n[4] Построение графика y = x^2 с matplotlib:")
    print(f"    График успешно сохранён: {saved_path}")

    # 5. Задание 10 (повышенное): Сериализация в JSON
    demo_data = {
        "lab_number": 2,
        "variant": 6,
        "student": {
            "name": "Вафин Денис Наильевич",
            "group": "221141",
            "department": "МИТП"
        },
        "completed_tasks": {
            "medium": [
                {"id": 2, "name": "Сумма нечётных чисел до N", "result": odd_sum},
                {"id": 6, "name": "Калькулятор", "tested": True},
                {"id": 8, "name": "Перевернуть строку", "sample": reversed_text}
            ],
            "advanced": [
                {"id": 4, "name": "График y=x^2 (matplotlib)", "file": plot_file},
                {"id": 10, "name": "Сериализация в JSON", "status": "active"}
            ]
        }
    }
    json_path = "data.json"
    serialize_data(demo_data, filepath=json_path)
    loaded_data = deserialize_data(filepath=json_path)
    print("\n[5] Сериализация данных в JSON:")
    print(f"    Файл сохранён: {os.path.abspath(json_path)}")
    print(f"    Десериализация успешна: студент '{loaded_data['student']['name']}'")
    print("=" * 60)


if __name__ == "__main__":
    main()
