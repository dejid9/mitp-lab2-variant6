"""Модуль для операций со строками."""


def reverse_string(text: str) -> str:
    """Переворачивает строку задом наперёд.

    Параметры:
        text (str): Исходная строка.

    Возвращает:
        str: Перевёрнутая строка.
    """
    if not isinstance(text, str):
        raise TypeError(f"Ожидалась строка, получено: {type(text).__name__}")
    return text[::-1]
