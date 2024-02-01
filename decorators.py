import time
from functools import wraps
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который спрашивает как дела и сам же на этот вопрос и отвечает :)
    :param func: Callable :return: Callable
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Функция обертка """
        print('Как дела? Хорошо.\nА у меня не очень! Ладно, держи свою функцию.')
        return func(*args, **kwargs)

    return wrapper


def code_slowdown(func: Callable) -> Callable:
    """
    Декоратор. Замедляет время выполнения декорируемой функции
    :param func: Callable :return: Callable
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Функция обертка """
        print('Немного терпения...')
        time.sleep(2)
        return func(*args, **kwargs)

    return wrapper


if __name__ == '__main__':
    @code_slowdown
    @how_are_you
    def test():
        print('<Тут что-то происходит...>')


    test()
