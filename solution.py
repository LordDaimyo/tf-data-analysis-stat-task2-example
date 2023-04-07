import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 712647540 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Найдем коэффициент ускорения
    t = 53 # время измерения в секундах

    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    # Найдем квантили нормального распределения
    z_alpha_half = norm.ppf(1 - alpha / 2)

    # Найдем среднее значение экспоненциального распределения
    mu = 1 / 2

    # Найдем стандартное отклонение экспоненциального распределения
    sigma = np.sqrt(2)

    # Найдем значение функции g, входящей в выражение для коэффициента ускорения
    g = (2 * (z_alpha_half ** 2) * (sigma ** 2)) + 1

    # Найдем значение коэффициента ускорения
    a = (g / mu) * (1 / (53 ** 2))

    # Найдем значение стандартного отклонения коэффициента ускорения
    sigma_a = np.sqrt((g ** 2) / (mu ** 2)) * (1 / (53 ** 2)) * np.sqrt(1 / (2 * (g - 1)))

    # Найдем левую и правую границы доверительного интервала
    left = a - z_alpha_half * sigma_a
    right = a + z_alpha_half * sigma_a

    return left, right
