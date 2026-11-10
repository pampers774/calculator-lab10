"""Учебный модуль с дефектной функцией деления (раздел 4 занятия 10)."""


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
