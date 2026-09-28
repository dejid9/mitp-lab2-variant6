"""Модуль построения графиков функций с помощью matplotlib."""

import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402


def plot_parabola(
    x_min: float = -10.0,
    x_max: float = 10.0,
    points: int = 400,
    output_path: str = "parabola.png"
) -> str:
    """Строит график квадратичной функции y = x^2 и сохраняет его в файл.

    Параметры:
        x_min (float): Левая граница аргумента x.
        x_max (float): Правая граница аргумента x.
        points (int): Количество точек дискретизации.
        output_path (str): Путь для сохранения изображения.

    Возвращает:
        str: Абсолютный путь к сохранённому файлу.
    """
    if x_min >= x_max:
        raise ValueError("x_min должен быть строго меньше x_max")
    if points < 2:
        raise ValueError("points должен быть не меньше 2")

    x = np.linspace(x_min, x_max, points)
    y = x ** 2

    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label=r"$y = x^2$", color="#0066cc", linewidth=2.0)
    plt.title("График квадратичной функции $y = x^2$", fontsize=14, fontweight="bold")
    plt.xlabel("Ось X", fontsize=11)
    plt.ylabel("Ось Y", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.axhline(0, color="black", linewidth=0.8)
    plt.axvline(0, color="black", linewidth=0.8)
    plt.legend(loc="upper center", fontsize=11)
    plt.tight_layout()

    plt.savefig(output_path, dpi=150)
    plt.close()
    return os.path.abspath(output_path)
