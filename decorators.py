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
