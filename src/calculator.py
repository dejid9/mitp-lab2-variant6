"""Модуль калькулятора с поддержкой основных арифметических операций."""


def calculate(a: float, b: float, op: str) -> float:
    """Выполняет арифметическую операцию над двумя числами.

    Поддерживаемые операции: '+', '-', '*', '/', '**', '//', '%'.

    Параметры:
        a (float): Первый операнд.
        b (float): Второй операнд.
        op (str): Знак операции.

    Возвращает:
        float: Результат вычисления.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Операнды должны быть числами")

    op = op.strip()
    if op == "+":
        return float(a + b)
    if op == "-":
        return float(a - b)
    if op == "*":
        return float(a * b)
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return float(a / b)
    if op == "**":
        return float(a ** b)
    if op == "//":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль при целочисленном делении")
        return float(a // b)
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("Деление на ноль при вычислении остатка")
        return float(a % b)

    raise ValueError(f"Неизвестная операция: {op}")
