"""Модуль для структурированной сериализации и десериализации данных в JSON."""

import json
from typing import Any


def serialize_data(data: Any, filepath: str | None = None, indent: int = 4) -> str:
    """Сериализует Python-структуру данных в JSON-строку и опционально в файл.

    Параметры:
        data (Any): Данные для сериализации (словарь, список и т.д.).
        filepath (str | None): Путь к файлу для сохранения (опционально).
        indent (int): Количество пробелов для отступа.

    Возвращает:
        str: Строка в формате JSON с поддержкой Unicode.
    """
    json_str = json.dumps(data, indent=indent, ensure_ascii=False)
    if filepath is not None:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(json_str)
    return json_str


def deserialize_data(json_str: str | None = None, filepath: str | None = None) -> Any:
    """Десериализует данные из JSON-строки или файла обратно в Python-объект.

    Параметры:
        json_str (str | None): JSON-строка.
        filepath (str | None): Путь к JSON-файлу.

    Возвращает:
        Any: Десериализованный объект Python.
    """
    if filepath is not None:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    if json_str is not None:
        return json.loads(json_str)
    raise ValueError("Необходимо передать json_str либо filepath")
