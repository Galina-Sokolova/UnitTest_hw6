# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
import numpy


def calculation_pearson_correlation(x, y):
    if len(x) != len(y):
        raise ValueError("Массивы должны быть одинаковой длины")
    else:
        x_avg = numpy.mean(x)
        y_avg = numpy.mean(y)
        numerator = sum((x_i - x_avg) * (y_i - y_avg) for x_i, y_i in zip(x, y))
        denominator = numpy.sqrt(sum((x_i - x_avg) ** 2 for x_i in x) * sum((y_i - y_avg) ** 2 for y_i in y))
        correlation = numerator / denominator
        return correlation


arr1 = [1, 2, 3, 6, 7]
arr2 = [10, 20, 29, 31, 23]
print("Корреляция Пирсона между массивами:", calculation_pearson_correlation(arr1, arr2))
