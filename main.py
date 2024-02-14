from decorators import how_are_you, code_slowdown, logging, counter, cashing


@counter
@logging
@code_slowdown
@how_are_you
def test():
    """ Функция для тестирования декораторов """
    print('<Тут что-то происходит...>')
    print(1 / 0)


@cashing
@counter
def fibonacci(number: int):
    if number <= 2:
        return 1
    return fibonacci(number - 2) + fibonacci(number - 1)


print(fibonacci(10))
print(fibonacci(11))
