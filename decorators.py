import datetime
import time
from functools import wraps
from typing import Callable


def how_are_you(func: Callable) -> Callable:
    """
    Декоратор, который спрашивает как дела и сам же на этот вопрос и отвечает:)
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


def logging(func: Callable) -> Callable:
    """
    Декоратор. Осуществляет логирование выполнения функций. Записывает ошибки возникающие в ходе выполнения
    декорируемой функции
    :param func: Callable :return: Callable
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Функция обертка """
        print(func.__name__, func.__doc__, sep='\n')
        try:
            func(*args, **kwargs)
        except Exception as error:
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write(f"\n{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - в ходе выполнения функции"
                           f" {func.__name__} произошла ошибка - {error}")

    return wrapper


def counter(func: Callable) -> Callable:
    """
    Декоратор. Осуществляет подсчет количества запуска функций.
    :param func: Callable :return: Callable
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """ Функция обертка """
        wrapper.count += 1
        print(f'Количество вызовов функции {func.__name__}: {wrapper.count}')
        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper


if __name__ == '__main__':
    @counter
    @logging
    @code_slowdown
    @how_are_you
    def test():
        """ Функция для тестирования декораторов """
        print('<Тут что-то происходит...>')
        # print(12 / 3)

    @counter
    @logging
    @code_slowdown
    def say_hello(name: str):
        """ Функция для приветствия пользователя """
        print('Hello', name)


    test()
    test(123)
    test()

    say_hello('Аня')
    say_hello('Антон')
