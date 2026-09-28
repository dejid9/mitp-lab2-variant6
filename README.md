# Лабораторная работа №2

ФИО: Вафин Денис Наильевич
Группа: 221141
Вариант: 6
Лабораторная работа: №2

Дисциплина: «Методы и технологии программирования».

## Выполненные практические задания по варианту 6

### Средней сложности
1. **№2 — Сумма всех нечётных чисел до N.** Реализована функция `sum_odd_numbers(n: int) -> int` с валидацией входных данных и обработкой граничных значений.
2. **№6 — Калькулятор.** Реализована функция `calculate(a: float, b: float, op: str) -> float`, поддерживающая операции `+`, `-`, `*`, `/`, `**`, `//`, `%`, а также обработку деления на ноль (`ZeroDivisionError`) и неизвестных операторов (`ValueError`).
3. **№8 — Перевернуть строку.** Реализована функция `reverse_string(text: str) -> str` с полной поддержкой Unicode и граничных случаев (пустая строка, палиндромы).

### Повышенной сложности
1. **№4 — Построить график y=x^2 с matplotlib.** Реализован модуль `src/plotting.py`, генерирующий оформленный график квадратичной параболы с координатной сеткой, осями и легендой, сохраняющий результат в графический файл `parabola.png`.
2. **№10 — Сериализация данных в JSON.** Реализован модуль `src/serializer.py` с функциями `serialize_data` и `deserialize_data` для персистентности данных в формате JSON с поддержкой Unicode-символов и отступов.

---

## Архитектура проекта

```text
mitp-lab2-variant6/
├── src/
│   ├── calculator.py       # Задание 6 (среднее): калькулятор
│   ├── number_series.py    # Задание 2 (среднее): сумма нечётных чисел
│   ├── plotting.py         # Задание 4 (повышенное): построение графика matplotlib
│   ├── serializer.py       # Задание 10 (повышенное): сериализация/десериализация JSON
│   └── strings_ops.py      # Задание 8 (среднее): переворот строки
├── tests/
│   └── test_lab2.py        # Набор модульных тестов pytest (12 тестов)
├── .flake8                 # Конфигурация линтера flake8
├── .gitattributes          # Нормализация переносов строк (eol=lf)
├── .gitignore              # Игнорируемые файлы Python/виртуального окружения
├── data.json               # Результат сериализации JSON
├── main.py                 # Точка входа для демонстрации всех заданий
├── parabola.png            # Построенный график y = x^2
├── README.md               # Документация и отчёт по лабораторной работе
└── requirements.txt        # Список зависимостей проекта
```

---

## Установка и запуск

### Вариант 1: Windows (PowerShell)

```powershell
# 1. Создание и активация виртуального окружения
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск демонстрации
python main.py

# 4. Проверка стиля кода через flake8
python -m flake8 .

# 5. Запуск набора тестов pytest
python -m pytest -v
```

### Вариант 2: Linux / macOS (Bash)

```bash
# 1. Создание и активация виртуального окружения
python3 -m venv .venv
source .venv/bin/activate

# 2. Установка зависимостей
pip install -r requirements.txt

# 3. Запуск демонстрации
python3 main.py

# 4. Проверка стиля кода через flake8
python3 -m flake8 .

# 5. Запуск набора тестов pytest
python3 -m pytest -v
```

---

## Подтверждение работы (логи выполнения)

### Демонстрация работы `main.py`:
```text
============================================================
Лабораторная работа №2 — Вариант 6
Дисциплина: «Методы и технологии программирования»
Студент: Вафин Денис Наильевич (Группа 221141)
============================================================

[1] Сумма нечётных чисел до 15: 64
    Ряд: [1, 3, 5, 7, 9, 11, 13, 15]

[2] Калькулятор (25.0 и 4.0):
    25.0 + 4.0 = 29.0
    25.0 - 4.0 = 21.0
    25.0 * 4.0 = 100.0
    25.0 / 4.0 = 6.25
    25.0 ** 4.0 = 390625.0
    25.0 // 4.0 = 6.0
    25.0 % 4.0 = 1.0

[3] Переворот строки:
    Исходная:   'Методы и технологии программирования 2026'
    Результат:  '6202 яинавориммаргорп ииголонхет и ыдотеМ'

[4] Построение графика y = x^2 с matplotlib:
    График успешно сохранён: C:\Users\dejid\Desktop\Учёба\Новая папка\mitp-lab2-variant6\parabola.png

[5] Сериализация данных в JSON:
    Файл сохранён: C:\Users\dejid\Desktop\Учёба\Новая папка\mitp-lab2-variant6\data.json
    Десериализация успешна: студент 'Вафин Денис Наильевич'
============================================================
```

### Результат проверки линтером `flake8`:
```text
python -m flake8 .
[OK] Ошибок не обнаружено, код полностью соответствует PEP 8.
```

### Результаты тестирования `pytest -v`:
```text
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.1.1, pluggy-1.6.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.12.6', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '9.1.1', 'pluggy': '1.6.0'}, 'Plugins': {'anyio': '4.15.1', 'html': '4.0.2', 'metadata': '3.1.1', 'ordering': '0.6', 'rerunfailures': '16.4', 'xdist': '3.8.0', 'seleniumbase': '4.51.3'}}
rootdir: C:\Users\dejid\Desktop\Учёба\Новая папка\mitp-lab2-variant6
plugins: anyio-4.15.1, html-4.0.2, metadata-3.1.1, ordering-0.6, rerunfailures-16.4, xdist-3.8.0, seleniumbase-4.51.3
collecting ... collected 17 items

tests/test_lab2.py::TestSumOddNumbers::test_positive_odd_bound PASSED    [  5%]
tests/test_lab2.py::TestSumOddNumbers::test_positive_even_bound PASSED   [ 11%]
tests/test_lab2.py::TestSumOddNumbers::test_single_element PASSED        [ 17%]
tests/test_lab2.py::TestSumOddNumbers::test_zero_and_negative PASSED     [ 23%]
tests/test_lab2.py::TestSumOddNumbers::test_invalid_type PASSED          [ 29%]
tests/test_lab2.py::TestCalculator::test_basic_arithmetic PASSED         [ 35%]
tests/test_lab2.py::TestCalculator::test_additional_operators PASSED     [ 41%]
tests/test_lab2.py::TestCalculator::test_zero_division PASSED            [ 47%]
tests/test_lab2.py::TestCalculator::test_invalid_operator PASSED         [ 52%]
tests/test_lab2.py::TestReverseString::test_simple_reverse PASSED        [ 58%]
tests/test_lab2.py::TestReverseString::test_empty_string PASSED          [ 64%]
tests/test_lab2.py::TestReverseString::test_palindrome PASSED            [ 70%]
tests/test_lab2.py::TestReverseString::test_unicode_and_spaces PASSED    [ 76%]
tests/test_lab2.py::TestPlotting::test_plot_generation PASSED            [ 82%]
tests/test_lab2.py::TestPlotting::test_invalid_bounds PASSED             [ 88%]
tests/test_lab2.py::TestJsonSerialization::test_roundtrip_dict PASSED    [ 94%]
tests/test_lab2.py::TestJsonSerialization::test_deserialize_from_string PASSED [100%]

============================= 17 passed in 2.16s ==============================
```

---

## Git Flow и ветвление

В репозитории строго соблюдена модель ветвления Git Flow:
- `main` — стабильная ветка релиза;
- `develop` — ветка интеграции разработки;
- `feature/variant6-impl` — функциональная ветка разработки заданий варианта 6;
- Слияния выполнены исключительно merge-коммитами с флагом `--no-ff` для сохранения прозрачной истории графа;
- Релиз зафиксирован аннотированным тегом `v1.0.0`.
